## Zarzuty

1. **Zakładasz, że sentyment głównych stron inwestycyjnych ma wartość predykcyjną. Co jeśli nie?** Serwisy takie jak MarketWatch czy Motley Fool publikują treści już PO ruchu cenowym — to echo rynku, nie sygnał wyprzedzający. Do tego dochodzi problem manipulacji: strony finansowe bywają wykorzystywane do pump-and-dump. Twoja aplikacja zbudowana na takich danych może systematycznie kupować szczyty. Bez backtestu na danych historycznych ("czy sygnał sentymentu z marca 2022 przewidział cokolwiek?") budujesz drogą maszynę do generowania szumu.

2. **"Jedna rekomendacja dziennie" to nie funkcja, to arbitralna decyzja bez uzasadnienia.** Dlaczego jedna? Rynek nie generuje okazji w regularnych odstępach. Albo tracisz okazje (bo limit dzienny), albo generujesz fałszywe (bo musisz coś wydać). To drugie jest gorsze — zmusza system do produkowania sygnału nawet, gdy sygnału nie ma.

3. **Koszty będą wyższe niż zakładasz, a wartość niższa.** Scraping + LLM + utrzymanie parserów (strony zmieniają strukturę, blokują boty, ToS tego zabrania) to realnie kilka godzin pracy tygodniowo na samym utrzymaniu. Alternatywa kosztuje 0$: darmowe newslettery, r/stocks, StockTwits, gotowe narzędzia typu TipRanks. Musisz odpowiedzieć: co Twoja aplikacja zrobi lepiej niż darmowa alternatywa? "Personalizacja" to nie odpowiedź, dopóki nie pokażesz, CO konkretnie personalizujesz.

4. **Prawdziwy problem to prawdopodobnie nie brak informacji, tylko Twoja dyscyplina.** Masz dostęp do więcej informacji niż każdy inwestor w historii. Jeśli mimo to nie podejmujesz dobrych decyzji, aplikacja dostarczająca jeszcze szybszych sygnałów pogorszy sprawę — będziesz handlować częściej, częściej oznacza więcej prowizji i więcej błędów. To zarzut kluczowy: budujesz narzędzie, które może działać przeciwko swojemu użytkownikowi.

5. **"Rekomendacja" słownie i funkcjonalnie.** Nawet dla własnego użytkoku warto wiedzieć: jeśli kiedykolwiek pokażesz to komuś (a ambicje zwykle rosną), wchodzisz w regulowane doradztwo inwestycyjne. Projektując system od początku jako "analiza danych" zamiast "rekomendacje", oszczędzasz sobie problem.

## Co mnie przekonałoby

- **Backtest na min. 12 miesiącach danych historycznych**: zbierz archiwalne nagłówki, policz sentyment, sprawdź korelację z rzeczywistymi zwrotami w oknach 1/7/30 dni. Jeśli korelacja jest statystycznie istotna — masz rację, ja się mylę, i to jest fundament, od którego trzeba zacząć. To kosztuje ~złotów, a odpowiada na pytanie nr 3 z agendy.
- **MVP bez LLM i bez scrapingu**: RSS feedy 3-5 źródeł (legalne, stabilne, darmowe), gotowy model sentymentu, codzienny e-mail. Koszt bliski zeru, testowalne w tydzień. Jeśli to nie zadziała, rozbudowana wersja tym bardziej nie.
- **Jasna odpowiedź na pytanie "co jeśli nie?"**: co zrobisz, gdy 6 miesięcy sygnałów okaże się gorszych niż losowy wybór? Jeśli masz plan wyjścia/weryfikacji, to traktujesz to jak eksperyment. Jeśli nie — jak wiarę.
- **Zdefiniowanie, co personalizacja oznacza w praktyce**: np. "filtruj pod mój portfel i horyzont 5 lat, ignoruj sygnały krótkoterminowe" — to byłoby realnie lepsze niż gotowe narzędzia.

Zacznij od backtestu. Wszystko inne to budowanie domu bez sprawdzenia gruntu.