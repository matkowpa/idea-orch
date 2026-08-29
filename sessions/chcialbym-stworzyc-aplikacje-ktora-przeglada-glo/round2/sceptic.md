## Zarzuty

1. **Nadal nie odpowiedziałeś na najważniejsze pytanie: co jeśli sentyment nie przewiduje niczego?** Runda 1 to wyłuszczyła, a Ty wracasz z tym samym pomysem bez backtestu. Główne strony inwestycyjne publikują treści PO ruchu cen — to echo, nie sygnał. Co więcej: sentyment głównych serwisów jest systematycznie spóźniony *i* podatny na manipulację (pump-and-dump żywi się dokładnie takimi nagłówkami). Twoja aplikacja w najgorszym wariantcie to automat do kupowania szczytów. Zanim wydasz złotówkę na cokolwiek innego, odpowiedz: czy sentyment z marca 2022 korelował z cenami w kwietniu 2022? To kosztuje weekend i darmowe archiwa RSS.

2. **"Jedna rekomendacja dziennie + okazje w ciągu dnia" — wewnętrzna sprzeczność, którą ignorujesz.** Jeśli rynek generuje sygnały nieregularnie, to masz dwa warianty: (a) limit dzienny = tracisz okazje, (b) brak limitu = generujesz szum. Twoja formuła "1 dziennie + dodatkowe" to wariant (b) z kosmetyką. Do tego "ciekawa okazja" nie ma zdefiniowanego progu — czyli de facto LLM zdecyduje, co jest okazją. To nie jest system inwestycyjny, to generator impulsów do klikania.

3. **Prawdziwy problem to Twoja dyscyplina, nie brak informacji — i budujesz narzędzie, które ją pogorszy.** Masz już nadmiar danych. Aplikacja dostarczająca *szybszych* sygnałów zwiększy częstotliwość transakcji, prowizje i błędy. Nie odpowiedziałeś na to wcale. Co jeśli aplikacja działa przeciwko Tobie? Jaka metryka to wykaże — i po jakim czasie odłożysz ją na półkę?

4. **Koszty są niedoszacowane, a alternatywa darmowa.** Scraping wymaga utrzymania parserów (strony zmieniają strukturę, blokują boty, ToS tego zabrania — kilka godzin tygodniowo na samym utrzymaniu). LLM w pętli to realne pieniądze miesięcznie. Darmowa alternatywa: RSS + newslettery + StockTwits = 0 zł. Musisz pokazać, co konkretnie robisz lepiej. "Personalizacja" to puste słowo, dopóki nie sprecyzujesz parametrów (portfel? horyzont? sektor? styl?) i czym to funkcjonalnie różni się od filtrów w TipRanks.

5. **Regulacyjne ryzyko nie zniknęło, bo piszesz "dla mnie wyłącznie".** Ambicje rosną — visionary już proponuje fazy 2 i 3 (SaaS, B2B white-label). Słowo "rekomendacja" w interfejsie, nawet prywatnym, utrwala architekturę produktu, która przy pierwszym udostępnieniu komukolwiek staje się regulowanym doradztwem (MiFID II). Projektuj od początku jako "analiza danych", nie "rekomendacje" — kosztuje zero teraz, oszczędza prawnika później.

6. **Plan visionary to budowanie zamku na gruncie, którego nikt nie zbadał.** Faza 2 (predefiniowane profile), faza 3 (community layer), B2B white-label — wszystko to zakłada, że sygnał *działa*. Bez backtestu to piramida założeń. Każda godzina poświęcona na architekturę skalowania przed walidacją sygnału to godzina wyrzucona.

## Co mnie przekonałoby

- **Backtest 12 miesięcy, zanim cokolwiek zbudujesz**: archiwalne nagłówki z RSS, gotowy model sentymentu, korelacja z rzeczywistymi zwrotami w oknach 1/7/30 dni. Koszt ~0 zł, czas ~tydzień. Istotna statystycznie korelacja = mam rację, że się mylę, i fundament jest.
- **MVP bez LLM i bez scrapingu**: 3–5 legalnych źródeł RSS, prosty model, codzienny mail, koszt bliski zeru. Jeśli to nie działa, rozbudowana wersja tym bardziej nie.
- **Zdefiniowany próg "okazji"**: konkretna reguła (np. "sentyment > X przy wolumenie > Y"), nie "LLM uzna, że ciekawe". Plus: co robi system w dzień bez sygnału — pomija, czy wymyśla?
- **Plan wyjścia**: co robisz, gdy po 6 miesiącach sygnały są gorsze niż losowość? Jeśli masz odpowiedź — to eksperyment. Jeśli nie — wiara.
- **Personalizacja w liczbach**: "filtruj pod mój portfel i horyzont 5 lat, ignoruj momentum" — to byłby realny, testowalny wyróżnik.

Zacznij od backtestu. Wszystko inne — w tym cała droga do SaaS — to dom na niezbadanym gruncie.