// Methode D: unabhaengige Implementierung der binaeren Goldbach-Verifikation
// in Go. Unabhaengig von den Python-Methoden A/B/C (eigene Sprache, eigenes
// ungerades Bitsieb, eigene Witness-Suche, parallele Chunks mit nachgelagerter
// sequenzieller Statistik).
//
// Kein Beweis von G_bin fuer alle n — endliche Verifikation auf [4, N].
//
// Witness-Datei (identisches Format zu Methode C, siehe ANLEITUNG.md):
//   "GBWIT1\n" + "<N>\n" + LEB128-Varints (minimales p fuer n=4,6,...,N)
//   + 4 Bytes CRC32 (IEEE, little-endian) ueber den Payload.
package main

import (
	"bufio"
	"encoding/binary"
	"flag"
	"fmt"
	"hash/crc32"
	"os"
	"runtime"
	"strconv"
	"sync"
	"sync/atomic"
	"time"
)

// PCAP: obere Schranke fuer gesuchte minimale Summandenprimzahlen.
// Fuer N <= 4e18 ist empirisch max min-p = 9781 (Oliveira e Silva et al.),
// daher ist 1<<20 großzuegig. Wird ein n nicht unter PCAP aufloesbar,
// zaehlt es als Fehlschlag (wird niemals stillschweigend ignoriert).
const PCAP = 1 << 20

var (
	sieve      []byte // Bitsieb: Bit i <-> ungerade Zahl 2i+1 ist prim
	oddPrimes  []uint32
	w16        []uint16 // w16[k-2] = minimales p fuer n=2k
	hist       []int64
	firstN     []int64 // erstes n mit Witness p
	failCount  int64
	firstFailN int64
)

func setBit(i int)      { sieve[i>>3] |= 1 << (uint(i) & 7) }
func clearBit(i int)    { sieve[i>>3] &^= 1 << (uint(i) & 7) }
func getBit(i int) bool { return sieve[i>>3]&(1<<(uint(i)&7)) != 0 }

// isPrime testet q in [2, N].
func isPrime(q int) bool {
	if q == 2 {
		return true
	}
	if q < 3 || q%2 == 0 {
		return false
	}
	return getBit((q - 1) / 2)
}

func buildSieve(N int) {
	half := N / 2 // Bit i <-> 2i+1
	sieve = make([]byte, half/8+2)
	for i := range sieve {
		sieve[i] = 0xFF
	}
	for i := 1; ; i++ {
		p := 2*i + 1
		if p*p > N {
			break
		}
		if !getBit(i) {
			continue
		}
		for m := p * p; m <= N; m += 2 * p {
			clearBit((m - 1) / 2)
		}
	}
	oddPrimes = make([]uint32, 0, 80000)
	for i := 1; 2*i+1 <= N && 2*i+1 <= PCAP; i++ {
		if getBit(i) {
			oddPrimes = append(oddPrimes, uint32(2*i+1))
		}
	}
}

func worker(kStart, kEnd int, wg *sync.WaitGroup) {
	defer wg.Done()
	for k := kStart; k <= kEnd; k++ {
		n := 2 * k
		w := uint16(0)
		if isPrime(n - 2) { // nur n=4 (n-2 gerade >2 ist nicht prim)
			w = 2
		} else {
			halfN := k
			for _, p := range oddPrimes {
				if int(p) > halfN {
					break
				}
				if isPrime(n - int(p)) {
					w = uint16(p)
					break
				}
			}
		}
		if w == 0 {
			c := atomic.AddInt64(&failCount, 1)
			if c == 1 {
				atomic.StoreInt64(&firstFailN, int64(n))
			}
		}
		w16[k-2] = w
	}
}

func main() {
	N := flag.Int("N", 200000, "gerade Obergrenze N >= 4")
	witnessPath := flag.String("witness", "", "optional: Pfad der Witness-Datei")
	outPath := flag.String("out", "", "optional: Pfad der Ergebnisdatei")
	flag.Parse()

	if *N < 4 || *N%2 != 0 {
		fmt.Fprintln(os.Stderr, "N muss gerade und >= 4 sein")
		os.Exit(2)
	}
	t0 := time.Now()

	buildSieve(*N)
	kmax := *N / 2
	w16 = make([]uint16, kmax-1) // k = 2..kmax
	hist = make([]int64, PCAP+1)
	firstN = make([]int64, PCAP+1)

	workers := runtime.NumCPU()
	if workers > 16 {
		workers = 16
	}
	chunk := (kmax - 1) / workers
	if chunk == 0 {
		chunk = 1
	}
	var wg sync.WaitGroup
	for kStart := 2; kStart <= kmax; kStart += chunk {
		kEnd := kStart + chunk - 1
		if kEnd > kmax {
			kEnd = kmax
		}
		wg.Add(1)
		go worker(kStart, kEnd, &wg)
	}
	wg.Wait()

	// Sequenzielle Statistik über w16 (Reihenfolge deterministisch).
	maxP := 0
	blocks := []struct{ a, b, m, firstN int }{}
	decadeMax, decadeFirst, decadeA := 0, 0, 4
	mag := 1
	for k := 2; k <= kmax; k++ {
		p := int(w16[k-2])
		if p == 0 {
			continue
		}
		if p > maxP {
			maxP = p
		}
		hist[p]++
		if firstN[p] == 0 {
			firstN[p] = int64(2 * k)
		}
		n := 2 * k
		if n > decadeB(decadeA) {
			blocks = append(blocks, struct{ a, b, m, firstN int }{decadeA, decadeB(decadeA), decadeMax, decadeFirst})
			decadeA = decadeB(decadeA) + 1
			decadeMax, decadeFirst = 0, 0
			mag++
		}
		if n >= decadeA && p > decadeMax {
			decadeMax = p
			decadeFirst = n
		}
	}
	if decadeMax > 0 || decadeA <= *N {
		blocks = append(blocks, struct{ a, b, m, firstN int }{decadeA, *N, decadeMax, decadeFirst})
	}

	// Rekordhalter aus Histogramm+firstN (p aufsteigend).
	type rec struct {
		p, first, cnt int64
	}
	records := []rec{}
	runMax := 0
	for p := 2; p <= PCAP; p++ {
		if hist[p] == 0 {
			continue
		}
		if p > runMax {
			runMax = p
			records = append(records, rec{int64(p), firstN[p], hist[p]})
		}
	}

	elapsed := time.Since(t0)
	checked := int64(kmax - 1)
	fails := atomic.LoadInt64(&failCount)
	firstFail := atomic.LoadInt64(&firstFailN)

	lines := []string{
		"BINÄRE GOLDBACH-VERIFIKATION METHODE D (Go, ungerades Bitsieb, parallel)",
		fmt.Sprintf("Intervall: alle geraden n mit 4 <= n <= %d", *N),
		"Methode: ungerades Bitsieb (Bit i <-> 2i+1); Witness p per aufsteigender",
		"         Suche in ungeraden Primzahlen; p=2 nur fuer n=4 relevant;",
		"         parallele Chunks, deterministische sequenzielle Statistik.",
		fmt.Sprintf("Anzahl geprüfter gerader n: %d", checked),
		fmt.Sprintf("Anzahl Fehlschläge: %d", fails),
		fmt.Sprintf("Erster Fehlschlag: %s", i64opt(firstFail, fails)),
		fmt.Sprintf("Größtes minimales p(n): %d", maxP),
		fmt.Sprintf("Anzahl Primzahlen <= %d (ungerade, bis PCAP=%d): %d", *N, PCAP, len(oddPrimes)),
		fmt.Sprintf("Laufzeit_s: %.6f", elapsed.Seconds()),
		fmt.Sprintf("Go: %s", runtime.Version()),
		fmt.Sprintf("GOMAXPROCS/NumCPU: %d/%d", runtime.GOMAXPROCS(0), runtime.NumCPU()),
		"",
		"Rekordhalter (p, erstes n mit min-p = p, Anzahl n mit diesem Rekord):",
	}
	for _, r := range records {
		lines = append(lines, fmt.Sprintf("  p=%6d  n_erste=%12d  anzahl=%d", r.p, r.first, r.cnt))
	}
	lines = append(lines, "", "Maximales minimales p(n) pro Zehnerpotz-Block [A,B]:")
	for _, b := range blocks {
		lines = append(lines, fmt.Sprintf("  [%12d, %12d]  max_min_p=%6d  erstes_n=%12d", b.a, b.b, b.m, b.firstN))
	}
	lines = append(lines,
		"",
		"BEWEISSTATUS DIESES LAUFS:",
		"  Wenn Fehlschlaege=0: die Aussage gilt fuer alle geraden n in [4,N].",
		"  Daraus folgt NICHT die Aussage fuer alle geraden n >= 4.",
		"")
	if fails > 0 {
		lines = append(lines, fmt.Sprintf("FEHLSCHLAEGE VORHANDEN; erster bei n=%d — GGIN WIDERLEGT, PRUEFEN!", firstFail))
	} else {
		lines = append(lines, "KEINE Gegenbeispiele im Intervall.")
	}
	text := ""
	for _, l := range lines {
		text += l + "\n"
	}
	if *outPath != "" {
		os.WriteFile(*outPath, []byte(text), 0o644)
	}
	fmt.Print(text)

	if *witnessPath != "" {
		if err := writeWitness(*witnessPath, *N); err != nil {
			fmt.Fprintln(os.Stderr, "witness:", err)
			os.Exit(3)
		}
		fmt.Println("geschrieben:", *witnessPath)
	}
	if fails > 0 {
		os.Exit(1)
	}
}

func decadeB(a int) int { // a ist 10^j oder 4
	if a == 4 {
		return 10
	}
	j := 0
	for t := a; t >= 10; t /= 10 {
		j++
	}
	return a * 10
}

func i64opt(v int64, cond int64) string {
	if cond == 0 {
		return "None"
	}
	return strconv.FormatInt(v, 10)
}

func writeWitness(path string, N int) error {
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()
	bw := bufio.NewWriterSize(f, 1<<20)
	bw.WriteString("GBWIT1\n")
	bw.WriteString(strconv.Itoa(N))
	bw.WriteByte('\n')
	var varintBuf [10]byte
	crc := crc32.NewIEEE()
	payloadBuf := make([]byte, 0, 1<<20)
	flush := func() error {
		if len(payloadBuf) > 0 {
			crc.Write(payloadBuf)
			if _, err := bw.Write(payloadBuf); err != nil {
				return err
			}
			payloadBuf = payloadBuf[:0]
		}
		return nil
	}
	for k := 2; k <= N/2; k++ {
		p := int64(w16[k-2])
		if p == 0 {
			return fmt.Errorf("kein Witness fuer n=%d; Datei wuerde unvollstaendig", 2*k)
		}
		nb := binary.PutUvarint(varintBuf[:], uint64(p))
		payloadBuf = append(payloadBuf, varintBuf[:nb]...)
		if len(payloadBuf) >= 1<<19 {
			if err := flush(); err != nil {
				return err
			}
		}
	}
	if err := flush(); err != nil {
		return err
	}
	var trailer [4]byte
	binary.LittleEndian.PutUint32(trailer[:], crc.Sum32())
	_, err = bw.Write(trailer[:])
	if err != nil {
		return err
	}
	return bw.Flush()
}
