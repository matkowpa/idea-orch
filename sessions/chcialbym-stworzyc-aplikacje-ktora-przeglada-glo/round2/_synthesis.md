## Consensus
- Backtest historyczny (6–12 miesięcy) jest niezbędny przed dalszym rozwojem — wszyscy trzej agenci się zgadzają, że to warunek startowy, nie opcja.
- MVP powinien być bez LLM w pętli i bez agresywnego scrapingu — start od 3–5 legalnych źródeł RSS/API.
- Produkt powinien być pozycjonowany jako "informacja/analiza", nie "rekomendacja/doradztwo" — ze względu na ryzyko regulacyjne (MiFID II).
- "Jedna rekomendacja dziennie" jako sztywna reguła jest problematyczna — potrzeba jasno zdefiniowanego progu jakości sygnału, a nie limitu czasowego.
- Zaczynać jako osobisty POC/eksperyment, a nie od razu jako produkt komercyjny/SaaS.
- Personalizacja (portfel, horyzont, sektory) to potencjalny wyróżnik względem konkurencji (TipRanks, StockTwits) — ale wymaga konkretnej definicji.

## Spory (pytania do kolejnej rundy)
1. Czy backtest zostanie wykonany PRZED jakimikolwiek dalszymi decyzjami produktowymi/architektonicznymi (sceptic) — czy można równolegle projektować fazy 2/3 skalowania (visionary)?
2. Jaki konkretnie próg/reguła definiuje "sygnał" lub "okazję" (np. sentyment > X przy wolumenie > Y), a nie ocena LLM "na czuja"?
3. Co system robi w dniu bez sygnału — pomija komunikat, czy generuje coś sztucznie, żeby "było"?
4. Jaka metryka i po jakim czasie zdecyduje o zamknięciu/pivotcie projektu, jeśli backtest wypadnie negatywnie (plan wyjścia)?
5. Czy celem jest walidacja tezy predykcyjnej (sentyment przewiduje ceny), czy od razu redefinicja produktu jako "kuratora informacji" bez aspiracji predykcyjnych — kto i kiedy podejmuje tę decyzję?
6. Czym konkretnie "personalizacja" różni się funkcjonalnie od istniejących filtrów w TipRanks/StockTwits?

## Luki informacyjne
- Brak wykonanego backtestu — kluczowa luka blokująca ocenę całego pomysłu.
- Brak konkretnej definicji progu sygnału/"okazji".
- Brak zdefiniowanych parametrów personalizacji (portfel, horyzont, sektor, styl inwestycyjny).
- Brak jasnej decyzji, czy projekt zaczyna się jako czysty POC osobisty, czy z góry z ambicją komercyjną (wpływa na priorytety prawne/architektoniczne).
- Brak oszacowania rzeczywistych kosztów utrzymania parserów/API w czasie oraz planu na wypadek zmiany ToS źródeł.
- Brak informacji, czy autor ma zasoby (czas, umiejętności data science) do samodzielnego wykonania backtestu, czy potrzebuje pomocy zewnętrznej.

STATUS: CONTINUE