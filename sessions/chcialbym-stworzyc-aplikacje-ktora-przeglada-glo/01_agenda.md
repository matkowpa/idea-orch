## Agenda

- **Problem, który aplikacja rozwiązuje**: Czy realnym problemem jest brak czasu na analizę rynku, czy raczej brak umiejętności/dyscypliny inwestycyjnej? Trzeba rozgraniczyć "agregację informacji" od "podejmowania decyzji inwestycyjnych".

- **Grupa docelowa i jej realna potrzeba**: Projekt zaczyna jako narzędzie na własny użytek właściciela — czy to zostaje projektem osobistym, czy ma ambicję skalowania do innych użytkowników? To determinuje wszystkie kolejne decyzje.

- **Model monetyzacji**: Jeśli to tylko własne narzędzie, monetyzacja nie istnieje — koszty (API, scraping, LLM) trzeba jednak oszacować. Jeśli produkt komercyjny, pytanie o model (subskrypcja, freemium) i grupę płacącą.

- **Konkurencja i alternatywy**: Istnieje wiele narzędzi sentiment-analysis (np. Bloomberg, TipRanks, narzędzia AI dla traderów) oraz alternatywa "nie robić nic" i korzystać z newsletterów/analityków. Trzeba zweryfikować, czy własne rozwiązanie da przewagę nad gotowymi narzędziami.

- **Unikalność / przewaga**: Analiza sentymentu ze stron inwestycyjnych to technologia dostępna "off-the-shelf". Przewaga może leżeć w personalizacji (dopasowanie do własnego portfela/strategii), nie w samej technologii.

- **Ryzyka biznesowe i operacyjne**:
  - Prawne/ToS ryzyko scrapowania stron finansowych.
  - Jakość danych — sentyment ≠ trafna rekomendacja inwestycyjna (fałszywe sygnały, hype, manipulacje rynkowe).
  - Odpowiedzialność — czy aplikacja "rekomenduje" w sensie regulacyjnym (usługi inwestycyjne są regulowane prawnie).
  - Zależność od jakości źródeł i modeli NLP/LLM.

- **Zakres MVP**: Czy MVP to prosty scraper + gotowy model sentymentu + codzienny raport mailowy, czy od razu system alertów w czasie rzeczywistym? Warto zdefiniować minimalny, testowalny zakres na start (np. 3-5 źródeł, jedna klasa aktywów).

## Pytania do rady

1. Czy celem jest narzędzie osobiste (proof of concept) czy produkt do skalowania na innych użytkowników — bo to zmienia całą architekturę decyzji?
2. Jakie konkretne źródła danych planujemy analizować i czy mamy prawo/legalny dostęp do ich treści (ToS, API vs scraping)?
3. Jak zweryfikujemy, że "sentyment" faktycznie przekłada się na trafne rekomendacje — jaki jest plan na backtesting/walidację?
4. Czy aplikacja może zostać uznana za usługę doradztwa inwestycyjnego i jakie z tego wynikają obowiązki prawne?
5. Jaki jest najmniejszy zakres MVP, który pozwoli sprawdzić hipotezę bez nadmiernych kosztów (API/LLM) i czasu wdrożenia?