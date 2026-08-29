## Agenda

- **Problem i jego prawdziwa natura**: Czy przeciążenie informacyjne jest realnym problemem, czy raczej maskuje deficyt dyscypliny decyzyjnej użytkownika — a szybsze sygnały mogą go pogłębiać, nie leczyć.

- **Grupa docelowa i wielkość niszy**: Aktywni inwestorzy DIY z FinTwit/StockTwits to wąski, konkurencyjny segment — czy jest wystarczająco duży i skłonny płacić, gdy darmowe alternatywy istnieją.

- **Fundament wartości predykcyjnej (kluczowy blocker)**: Brak backtestu = brak dowodu, że sentyment ma jakąkolwiek wartość sygnałową. Cała reszta dyskusji jest warunkowa względem tego punktu.

- **Model monetyzacji vs. darmowa konkurencja**: Subskrypcja 10-40 EUR ma sens tylko jeśli udowodniona zostanie albo predykcyjność, albo mierzalna redukcja szumu/czasu — inaczej użytkownik nie zapłaci za to, co ma za 0 zł.

- **Konkurencja i przewaga**: Personalizacja i "anty-hałas" jako przewaga są deklaratywne — trzeba zdefiniować konkretnie, czym różnią się od istniejących filtrów TipRanks/Seeking Alpha/Dataminr.

- **Ryzyko regulacyjne (MiFID II)**: Pełny konsensus rady, że słowo "rekomendacja" i architektura produktu grożą wejściem w regulowane doradztwo inwestycyjne — wymaga rozstrzygnięcia pozycjonowania od startu.

- **Architektura produktu "1 sygnał dziennie"**: Sztywny limit jest wewnętrznie sprzeczny — prowadzi do utraty okazji albo generowania sztucznych sygnałów w dni bez treści. Wymaga przeprojektowania na próg jakości, nie częstotliwości.

- **Zakres MVP/POC**: Czy budować produkt komercyjny, czy najpierw osobisty POC do walidacji (RSS/API, 3-5 źródeł, prosty model, bez LLM/scrapingu) — sekwencja działań przed jakąkolwiek komercjalizacją.

- **Koszty operacyjne i zasoby**: Utrzymanie scraperów, ryzyko ToS, koszty LLM, oraz realne kompetencje/czas autora do samodzielnego wykonania rzetelnego backtestu.

## Pytania do rady

1. Czy backtest (6-12 mies.) jest warunkiem blokującym dalszy rozwój, czy można równolegle projektować architekturę produktu/skalowania?
2. Jaki konkretny, mierzalny próg zdefiniuje "sygnał" i kiedy uzna się backtest za sukces vs. porażkę (kill/continue)?
3. Co system robi w dniach bez wykrytego sygnału — cisza, informacja "brak okazji", czy wymuszony output?
4. Czym personalizacja różni się funkcjonalnie od istniejących filtrów konkurencji — da się to zdefiniować przed budową?
5. Czy autor ma zasoby (czas, kompetencje data science) do samodzielnego wykonania POC i backtestu, czy potrzebne jest partnerstwo/rekrutacja?