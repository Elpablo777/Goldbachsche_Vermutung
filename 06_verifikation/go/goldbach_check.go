// Methode D: unabhaengige Implementierung der binaeren Goldbach-Verifikation
// in Go. Unabhaengig von den Python-Methoden A/B/C (eigene Sprache, eigenes
// ungerades Bitsieb, eigene Witness-Suche, parallele Chunks mit nachgelagerter
// sequenzieller Statistik).
//
// Kein Beweis von G_bin fuer alle n — endliche Verifikation auf [A, N].
//
// Segmentmodus (-A > 4): prueft nur [A, N] (fuer CI-Matrix-Parallellaeufe).
// Das Sieb bleibt ein Voll-Sieb bis N (isPrime(n-p) braucht alle q <= N).
// Witness-Dateien:
//   A == 4: Format GBWIT1 ("GBWIT1\n" + "<N>\n" + Varints + CRC32)
//   A >  4: Format GBWITSEG1 ("GBWITSEG1\n" + "<N>\n" + "<A>\n" + Varints + CRC32)
// Varints: LEB128 des minimalen p fuer n = A, A+2, ..., N (in dieser Reihenfolge).
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
// Empirisch ist max min-p = 9781 bis 4e18 (Oliveira e Silva et al.); 1<<20
// ist großzuegig. Wird ein n nicht unter PCAP aufgeloest, zaehlt es als
// Fehlschlag (wird niemals stillschweigend ignoriert).
const PCAP = 1 << 20

var (
	sieve     []byte // Bitsieb: Bit i <-> ungerade Zahl 2i+1 ist prim
	oddPrimes []uint32
	w16       []uint16 // w16[k-kBase] = minimales p fuer n=2k
	kBase     int
	hist      []int64
	firstN    []int64 // erstes n (im Segment) mit Witness p
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
		w16[k-kBase] = w
	}
}

// nextBlockEnd liefert das kleinste Zehnerpotz-Ende > a (Bloecke [.., 10], (10,100], ...).
func nextBlockEnd(a int) int {
	b := 10
	for b <= a {
		b *= 10
	}
	return b
}

func main() {
	N := flag.Int("N", 200000, "gerade Obergrenze N >= 4 (Segmentende)")
	A := flag.Int("A", 4, "gerader Segmentstart >= 4 (Default 4 = Vollbereich)")
	witnessPath := flag.String("witness", "", "optional: Pfad der Witness-Datei")
	outPath := flag.String("out", "", "optional: Pfad der Ergebnisdatei")
	flag.Parse()

	if *N < 4 || *N%2 != 0 || *A < 4 || *A%2 != 0 || *A > *N {
		fmt.Fprintln(os.Stderr, "Bedingung verletzt: 4 <= A <= N, N gerade, A gerade")
		os.Exit(2)
	}
	t0 := time.Now()

	buildSieve(*N)
	kBase = *A / 2
	kmax := *N / 2
	w16 = make([]uint16, kmax-kBase+1) // k = kBase..kmax
	hist = make([]int64, PCAP+1)
	firstN = make([]int64, PCAP+1)

	workers := runtime.NumCPU()
	if workers > 16 {
		workers = 16
	}
	chunk := (kmax - kBase + 1) / workers
	if chunk == 0 {
		chunk = 1
	}
	var wg sync.WaitGroup
	for kStart := kBase; kStart <= kmax; kStart += chunk {
		kEnd := kStart + chunk - 1
		if kEnd > kmax {
			kEnd = kmax
		}
		wg.Add(1)
		go worker(kStart, kEnd, &wg)
	}
	wg.Wait()

	// Sequenzielle Statistik über w16 (Reihenfolge deterministisch).
	type block struct{ a, b, m, firstN int }
	blocks := []block{}
	blockA := *A
	blockEnd := nextBlockEnd(*A)
	if blockEnd > *N {
		blockEnd = *N
	}
	decadeMax, decadeFirst := 0, 0
	for k := kBase; k <= kmax; k++ {
		p := int(w16[k-kBase])
		if p == 0 {
			continue
		}
		hist[p]++
		if firstN[p] == 0 {
			firstN[p] = int64(2 * k)
		}
		n := 2 * k
		if n > blockEnd {
			blocks = append(blocks, block{blockA, blockEnd, decadeMax, decadeFirst})
			blockA = blockEnd + 1
			blockEnd = nextBlockEnd(blockA)
			if blockEnd > *N {
				blockEnd = *N
			}
			decadeMax, decadeFirst = 0, 0
		}
		if p > decadeMax {
			decadeMax = p
			decadeFirst = n
		}
	}
	blocks = append(blocks, block{blockA, *N, decadeMax, decadeFirst})

	// Rekordhalter aus Histogramm+firstN (p aufsteigend, innerhalb des Segments).
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
	checked := int64(kmax - kBase + 1)
	fails := atomic.LoadInt64(&failCount)
	firstFail := atomic.LoadInt64(&firstFailN)
	maxP := runMax

	segLabel := fmt.Sprintf("[%d, %d]", *A, *N)
	if *A == 4 {
		segLabel = fmt.Sprintf("[4, %d]", *N)
	}
	lines := []string{
		"BINÄRE GOLDBACH-VERIFIKATION METHODE D (Go, ungerades Bitsieb, parallel)",
		fmt.Sprintf("Intervall: alle geraden n mit %s", segLabel),
		fmt.Sprintf("Segmentmodus: A=%d, N=%d (Sieb bis N, Witness-Suche im Segment)", *A, *N),
		"Methode: ungerades Bitsieb (Bit i <-> 2i+1); Witness p per aufsteigender",
		"         Suche in ungeraden Primzahlen; p=2 nur fuer n=4 relevant;",
		"         parallele Chunks, deterministische sequenzielle Statistik.",
		fmt.Sprintf("Anzahl geprüfter gerader n: %d", checked),
		fmt.Sprintf("Anzahl Fehlschläge: %d", fails),
		fmt.Sprintf("Erster Fehlschlag: %s", i64opt(firstFail, fails)),
		fmt.Sprintf("Größtes minimales p(n) im Segment: %d", maxP),
		fmt.Sprintf("Anzahl ungerader Primzahlen bis PCAP=%d: %d", PCAP, len(oddPrimes)),
		fmt.Sprintf("Laufzeit_s: %.6f", elapsed.Seconds()),
		fmt.Sprintf("Go: %s", runtime.Version()),
		fmt.Sprintf("GOMAXPROCS/NumCPU: %d/%d", runtime.GOMAXPROCS(0), runtime.NumCPU()),
		"",
		"Rekordhalter im Segment (p, erstes n mit min-p = p, Anzahl n):",
	}
	for _, r := range records {
		lines = append(lines, fmt.Sprintf("  p=%6d  n_erste=%12d  anzahl=%d", r.p, r.first, r.cnt))
	}
	lines = append(lines, "", "Maximales minimales p(n) pro Block (Zehnerpotz-Grenzen, auf Segment beschnitten):")
	for _, b := range blocks {
		lines = append(lines, fmt.Sprintf("  [%12d, %12d]  max_min_p=%6d  erstes_n=%12d", b.a, b.b, b.m, b.firstN))
	}
	lines = append(lines,
		"",
		"BEWEISSTATUS DIESES LAUFS:",
		"  Wenn Fehlschlaege=0: die Aussage gilt fuer alle geraden n im Intervall.",
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
		if err := writeWitness(*witnessPath, *A, *N); err != nil {
			fmt.Fprintln(os.Stderr, "witness:", err)
			os.Exit(3)
		}
		fmt.Println("geschrieben:", *witnessPath)
	}
	if fails > 0 {
		os.Exit(1)
	}
}

func i64opt(v int64, cond int64) string {
	if cond == 0 {
		return "None"
	}
	return strconv.FormatInt(v, 10)
}

func writeWitness(path string, A, N int) error {
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()
	bw := bufio.NewWriterSize(f, 1<<20)
	if A == 4 {
		bw.WriteString("GBWIT1\n")
		bw.WriteString(strconv.Itoa(N))
		bw.WriteByte('\n')
	} else {
		bw.WriteString("GBWITSEG1\n")
		bw.WriteString(strconv.Itoa(N))
		bw.WriteByte('\n')
		bw.WriteString(strconv.Itoa(A))
		bw.WriteByte('\n')
	}
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
	for k := A / 2; k <= N/2; k++ {
		p := int64(w16[k-kBase])
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
