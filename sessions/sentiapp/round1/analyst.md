## Ocena rynku
- Wielkość i segment: realny adresowalny rynek to aktywni inwestorzy detaliczni / traderzy szukający kuracji treści (FinTwit/StockTwits/Reddit). To nisza w ramach rynku inwestycyjnego — szacunkowo kilkaset tys. do kilku milionów użytkowników w regionach UE/US zainteresowanych płatnymi narzędziami (szacunek, wymaga walidacji rynkowej po kraju).  
- Potencjał płatności: tylko niewielki odsetek tej grupy zapłaciabon/subskrypcję (konwersja freemium→płatne typowo 1–5%). Dlatego model B2C wymaga wyraźnego, mierzalnego ROI/usługi zastępczej dla użytkownika.

## Konkurencja
- Bezpośredni i pośredni: TipRanks, Seeking Alpha, StockTwits, Dataminr, AlphaSense, Zacks, Finviz, darmowe społeczności/ newslettery (FinTwit, subreddity).  
- Różnica konkurencyjna obecnie deklaratywna: personalizacja portfelowa + limit sygnałów ("anty-hałas"). Konkurenci mają już filtry, alerty i analizy; przewaga musi być technicznie i empirycznie udowodniona (np. dopasowanie sygnału do korelacji z konkretnym portfelem użytkownika).

## Monetyzacja
- Obecny model B2C subskrypcja 10–40 EUR/mies. ma sens tylko przy jednoznacznej, testowanej wartości (predykcyjna skuteczność lub oszczędność czasu).  
- Alternatywy: freemium z paywall na zaawansowaną personalizację, B2B/white-label (brokerzy, newslettery) — B2B lepsze przy braku wyraźnej alpha, bo płacą za UX/retencję użytkownika.  
- Wniosek: monetyzacja musi wynikać z konkretnej metryki wartości (np. poprawa sharpe/rentowności vs. benchmark, albo zmniejszenie czasu poświęconego na selekcję o X%).

## Wykonalność MVP
- MVP (POC osobisty) rekomendowany: 3–5 źródeł przez API/RSS, prosty rule-based sentiment (avoid HTML scraping), bez LLM w pętli. Backtest 6–12 mies. z jasno określonymi metriksami: hit rate, zwrot vs. benchmark, drawdown, turnover cost impact (wstępne progi kill/continue).  
- Koszty/zasoby MVP (szacunki): 1–2 osobomiesiące dev (integracje API, pipeline), 1–2 osobomiesiące data-science (backtest + walidacja), infrastruktura: ~200–800 EUR/mies. (hosting, bazy, API), dodatkowo koszty danych źródłowych/licencji jeśli wymagane (0–kilkaset EUR/mies.). Jeśli planujesz LLM — koszty rosną znacząco (zmienne).  
- Ryzyka techniczne: utrzymanie scraperów/ToS — unikaj scrapingu; preferuj oficjalne API/licencje. Regulacje: unikaj formułowania "rekomendacja"; pozycjonuj jako "analiza/informacja" i konsultuj prawnika przy skali.

Odpowiedzi na pytania z agendy
1. Czy backtest jest blokujący? Tak — backtest jest warunkiem sine qua non przed komercjalizacją sygnałów. Równoległe projektowanie architektury technicznej jest akceptowalne, ale nie inwestuj dużych zasobów w skalowanie bez wyników backtestu.  
2. Jaki próg dla "sukcesu" backtestu? Propozycja minimalna do rozważenia: przewaga statystyczna nad odpowiednim benchmarkiem (np. alfa > 0 przy uwzględnieniu kosztów transakcyjnych i komisji) oraz akceptowalny poziom drawdown; alternatywnie mierzalne ~30–50% redukcji czasu filtracji informacji dla user-experience. Konkretne progi muszą być ustalone przed testem.  
3. Co system robi w dniach bez sygnału? Domyślnie: cisza + opcjonalna informacja "brak okazji spełniającej twoje kryteria". Nie wymuszaj sygnału — komunikacja tego braku jest wartością (redukcja hałasu).  
4. Czym personalizacja różni się od filtrów konkurencji? Musi to być: 1) dopasowanie sygnałów do realnego składu portfela i horyzontu (np. waga, korelacja, stop-lossy użytkownika), 2) dynamiczne progi jakości sygnału zależne od profilu ryzyka, 3) transparentne reguły/wyjaśnienia ("dlaczego to sygnał dla twojego portfela"). Zdefiniuj te reguły przed budową.  
5. Czy autor ma zasoby do POC/backtestu? Jeśli autor nie ma solidnych kompetencji data science i dostępu do danych/historycznych cen/licencji, potrzebne partnerstwo lub zlecenie na 1–2 miesiące pracy DS. Samodzielnie możliwe tylko przy znacznym wkładzie czasu i nauce.

Rekomendacja: natychmiastowy osobisty POC + rygorystyczny backtest. Dopiero przy pozytywnym wyniku — przekształcenie w MVP komercyjne z jasno zdefiniowaną personalizacją i zgodnością regulacyjną.