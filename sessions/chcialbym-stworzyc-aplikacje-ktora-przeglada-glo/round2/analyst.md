## Ocena rynku
- Segment: aktywni inwestorzy detaliczni i półprofesjonalni szukający „przefiltrowanego” źródła pomysłów (daytraderzy okazjonalni, inwestorzy growth/momentum, operatorzy portfela DIY). Nie trafia do pasywnych inwestorów/ETF-only.  
- Wielkość rynku: (szacunek) potencjalny adresowalny rynek w UE/US dla płacących użytkowników B2C: setki tys. tysięcy — ale realny przyczepność zależy od skuteczności sygnałów i UX. Początkowo lepiej targetować niszę (np. FinTwit/StockTwits users).
- Rzeczywisty problem: bardziej brak czasu i „przefiltrowania” informacji niż edukacja — jednak to nie eliminuje ryzyka, że lepsze decyzje wymagają innych kompetencji. Aplikacja powinna być pozycjonowana jako narzędzie informacyjne, nie doradztwo.

## Konkurencja
- Bezpośrednie/pośrednie: TipRanks, Seeking Alpha, MarketPsych, Dataminr, AlphaSense (enterprise), SentimentPro tools, StockTwits, Reddit/FinTwit (darmowe).  
- Alternatywy: newslettery tematyczne, agregatory RSS, terminale (Bloomberg) — większość oferuje gotowe sygnały lub alerty, ale rzadko z mocną personalizacją pod portfel użytkownika.  
- Wyróżnik możliwy do zbudowania: personalizacja sygnałów względem portfela/horyzontu i ograniczanie liczby alertów („1 rekomendacja dziennie jako produkt UX”), plus rygor backtestu jako proof.

## Monetyzacja
- Model bazowy: subskrypcja B2C (freemium). Freemium: opóźnione/działowe sygnały + ograniczona liczba źródeł; płatne: real-time, personalizacja, integracja watchlisty. (Szacunek ceny): 10–30 EUR/mies.  
- Alternatywy: B2B/API/white-label dla mniejszych brokerów lub newsletterów; premium analytics dla hedge-fund-like users.  
- Ocena wartości→przychód: monetyzacja możliwa jeśli:
  1) sygnały poprawiają rezultaty vs. benchmark (weryfikowalne backtestem), lub  
  2) UX oszczędza znacząco czas użytkownika i redukuje hałas (wartość subskrypcji UX-driven).  
- Ryzyko: bez dowodu skuteczności konwersja na płatnych użytkowników będzie niska.

## Wykonalność MVP
- Minimalny zakres (zalecany): 3–5 legalnych źródeł (RSS/API — nie agresywny scraping), prosty model sentymentu (lexicon + prosty ML), backtest na 6–12 miesięcy historycznych nagłówków/treści, codzienny e-mail z maks. 1 rekomendacją i opcją „brak sygnału”.  
- Zasoby i czas (szacunek): 1 backend dev + 1 data scientist part-time na 4–8 tygodni => MVP; koszty chmurowe + dane: 200–1 200 USD/mies. (zależnie od źródeł i czy używasz płatnych modeli NLP).  
- Koszty operacyjne: utrzymanie parserów (czas dev), koszty API (news APIs ~50–500 USD/mies), opcjonalne LLM (jeśli użyte) znacząco zwiększają koszty — zacznij bez LLM.  
- Walidacja: obowiązkowy backtest (min. 6–12 m-cy). Metryki: hit rate sygnałów, zwrot vs. benchmark w oknach 1/7/30 dni, drawdown, liczba dni „brak sygnału”. Jeśli wyniki ≤ losowego/benchmark → pivot lub kill.  
- Ryzyka i mitigacje:
  - Prawne: sprawdzić ToS źródeł; preferować API/RSS; jasno komunikować „informacja, nie porada inwestycyjna”, disclaimery; rozważyć konsultację prawna w jurysdykcji (szacunek kosztu porady: 1–3k EUR).  
  - Manipulacje i szum: filtrowanie źródeł, detekcja anomalii (sudden volume of posts), limitowanie wpływu pojedynczego źródła.  
  - Produkt vs. regulacje: projektuj komunikaty jako „sygnały informacyjne” i unikaj instrukcji transakcyjnych; jeśli planujesz skalować komercyjnie, zbadaj czy lokalne prawo nie traktuje tego jako doradztwo.

Krótkie odpowiedzi na kluczowe pytania agendy:
1) Zacznij jako narzędzie osobiste/POC — to zmniejsza koszty i ryzyka; skaluj jeśli backtest i UX potwierdzą wartość.  
2) Wybierz konkretnie 3–5 źródeł z publicznym RSS/API i sprawdź ToS przed agregacją.  
3) Backtest 6–12 miesięcy to must — bez niego produkt jest eksperymentem bez podstaw.  
4) Pozycjonuj produkt jako „informacyjny”, przygotuj disclaimery i skonsultuj z prawnikiem przed komercjalizacją.  
5) Najmniejszy MVP: RSS/API + prosty model sentymentu + codzienny e-mail z możliwością „brak sygnału” — do wdrożenia w 4–8 tyg. przy niskim budżecie.