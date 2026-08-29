## Ocena rynku
- Segment: detaliczni inwestorzy aktywni (retail traders), entuzjaści tradingu społecznościowego i półprofesjonalni analitycy portfela, zainteresowani szybkim wyłapywaniem trendów z mediów/fora/news. Produkt trafia do użytkowników szukających sygnałów, nie pełnej analizy fundamentalnej.
- Wielkość rynku: globalny rynek narzędzi dla traderów detalicznych i subskrypcji finansowych jest istotny (szacunek: setki milionów użytkowników finansowo aktywnych globalnie; adresowalny rynek płacących użytkowników narzędzi premium — dziesiątki milionów). Dokładne TAM/SAM/SOM wymagają badań geograficznych i segmentacyjnych — to szacunki.
- Realna potrzeba: problem leży częściowo w braku czasu/filtra informacji oraz częściowo w potrzebie dyscypliny. Samo agregowanie sentymentu rozwiązuje pierwszy element; decyzje inwestycyjne i dyscyplina pozostają po stronie użytkownika.

## Konkurencja
- Bezpośrednie/pośrednie rozwiązania: TipRanks, Seeking Alpha (sentiment/analizy), Stocktwits, Benzinga, RavenPack (analytics), Dataminr, AlphaSense, Bloomberg terminaly (premium). Ponadto narzędzia wykorzystujące LLM do newsletterów/alertów (np. MarketSnacks-like, narzędzia typu SignalPop).
- Kategorie konkurencji: agregatory newsów, platformy social-sentiment, dostawcy danych alternatywnych i narzędzia AI dla traderów.
- Mocne strony konkurencji: dostęp do większych baz danych, licencjonowane źródła, wiarygodność. Twoja przewaga może być personalizacja rekomendacji pod konkretny portfel i prostota — "jedna rekomendacja dziennie".

## Monetyzacja
- Czy model wynika z wartości? Tak, jeśli aplikacja faktycznie dostarcza wyróżniającą, personalizowaną i skuteczną rekomendację — użytkownicy zapłacą subskrypcję za oszczędność czasu i lepsze decyzje.
- Proponowane modele: subskrypcja miesięczna/półroczna (core), freemium z ograniczonymi alertami, premium z integracją do brokerów/automatyzacją. Alternatywnie B2B licencje dla wealth managers.
- Ryzyko: trudność udowodnienia skuteczności — bez traceable backtestów ciężko przekonać płacących. Modele oparte na rekomendacjach muszą wyraźnie komunikować brak doradztwa regulowanego.

## Wykonalność MVP
- Minimalny MVP (zalecane): 3–5 źródeł (np. Reuters, r/WallStreetBets/StockTwits, Seeking Alpha, kilka blogów/serwisów lokalnych) + prosty scraper/API + gotowy model NLP/sentyment (open-source lub API LLM) + codzienny e-mail z jedną rekomendacją i opcjonalne intra-day alerty (push).
- Zasoby potrzebne:
  - Zespół: 1 backend dev (API/scraping), 1 data engineer/ML (pipeline + sentyment), 1 frontend/mobile dev (prosty UI + powiadomienia) — lub 2 full-stack devs + kontrakt ML.
  - Infrastruktura: serwer do scrappingu, baza danych, queuing, hosting powiadomień.
  - Koszty (szacunki miesięczne): scraping/hosting = 100–500 USD, API NLP/LLM (jeśli płatne) = 200–2000+ USD w zależności od użycia, płatne źródła/licencje = 0–kilkaset USD (w zależności od umów). Razem pierwszy rok MVP: minimalnie kilka tys. USD (szacunek).
- Legalność: sprawdzić ToS źródeł — preferować oficjalne API/licencje zamiast agresywnego scrapingu. Oceniać ryzyko regulacyjne (czy produkt to „doradztwo inwestycyjne”).
- Walidacja skuteczności: konieczny backtesting historyczny na sygnałach (przynajmniej 6–12 miesięcy danych) + test użytkowników (A/B) z metrykami: hit rate, P&L symulowane, czas reakcji. Bez tego trudno monetyzować.
- Czas wdrożenia MVP: 8–12 tygodni z małym zespołem (szacunek) przy ograniczonym zakresie źródeł i prostym modelu.

Odpowiedzi na pytania z agendy
1. Cel: musisz zdecydować teraz. Jeśli to POC osobisty — upraszcza to legalność i koszty; jeśli skalowanie — projekt wymaga innej architektury, legalnego dostępu do danych i silnej walidacji.
2. Źródła: wybierz 3–5 i sprawdź ToS/API. Preferuj publiczne API lub treści o jasno określonych zasadach użycia; unikaj scrapingu bez zgody.
3. Weryfikacja: backtesting sygnałów + statystyki trafności, testy na out-of-sample, eksperymenty użytkowników. Metryki: precision, recall, zwrot portfolio vs benchmark.
4. Regulacje: istnieje ryzyko uznania za doradztwo. Unikaj formułowania "kup/sprzedaj" jako porady; stosuj disclaimery, rozważ konsultację prawna i ewentualne licencje przy skalowaniu.
5. Najmniejszy MVP: scraper/API 3 źródeł + prosty sentyment + codzienny e-mail z 1 rekomendacją + dashboard podstawowych statystyk. Minimalne koszty i czas: ~2–3 miesiące, kilkaset–kilka tys. USD (szacunek).