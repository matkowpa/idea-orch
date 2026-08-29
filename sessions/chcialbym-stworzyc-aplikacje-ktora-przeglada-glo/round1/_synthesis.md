## Consensus
- Potrzebny jest backtest historyczny (min. 6-12 miesięcy) sygnałów sentymentu przed jakąkolwiek dalszą rozbudową – bez tego nie da się ocenić skuteczności.
- MVP powinien być minimalny: 3-5 źródeł, prosty model sentymentu/NLP, codzienny e-mail/alert, niski koszt, krótki czas budowy.
- Scraping niesie ryzyko prawne/ToS – lepiej oprzeć się na oficjalnych API/RSS niż na agresywnym scrapingu.
- Istnieje ryzyko regulacyjne związane z "rekomendacjami" inwestycyjnymi (MiFID i podobne) – produkt powinien być pozycjonowany jako narzędzie informacyjne, nie doradztwo.
- Personalizacja (pod portfel/profil użytkownika) jest wskazywana jako potencjalna przewaga konkurencyjna, ale wymaga konkretnego zdefiniowania.
- Konkurencja jest silna i zróżnicowana (TipRanks, Seeking Alpha, StockTwits, FinTwit, newslettery) – trzeba jasno wskazać różnicujący element.

## Spory (pytania do kolejnej rundy)
1. Czy aplikacja jest projektowana jako osobisty POC/eksperyment, czy od początku ma ambicję skalowania do produktu dla innych użytkowników? (Ma to wpływ na architekturę, prawo, koszty.)
2. Jak konkretnie ma wygląać "personalizacja" – jakie parametry (portfel, horyzont, sektor, styl inwestycyjny) i czym to się różni funkcjonalnie od istniejących narzędzi (TipRanks, Seeking Alpha)?
3. Czy "jedna rekomendacja dziennie" to świadomy wybór produktowy oparty na jakiejś logice, czy arbitralny limit – i co się dzieje, gdy rynek nie generuje sygnału tego dnia (system "wymyśla" sygnał czy pomija dzień)?
4. Jaki jest plan na wypadek, gdyby backtest wykazał, że sentyment nie ma wartości predykcyjnej (lub jest gorszy niż benchmark)? Jest to "eksperyment z punktem wyjścia" czy założenie nie do obalenia?
5. Czy istnieje realna przewaga nad darmowymi alternatywami (Reddit, StockTwits, newslettery) wystarczająca do uzasadnienia płatnej subskrypcji – i w czym konkretnie ta przewaga miałaby polegać?
6. Jak produkt zamierza uniknąć klasyfikacji jako regulowane doradztwo inwestycyjne w praktyce (nazewnictwo, format komunikatów, disclaimery) – czy jest to już przemyślane, czy odłożone na później?

## Luki informacyjne
- Brak danych o docelowym użytkowniku: to ma być tylko dla autora (POC) czy produkt komercyjny od startu?
- Brak konkretnego wyboru źródeł danych i sprawdzenia ich ToS/dostępności API.
- Brak zdefiniowanych metryk sukcesu (hit rate, zwrot vs benchmark, retencja użytkowników).
- Brak oszacowania budżetu i czasu, jaki autor faktycznie może/chce zainwestować (agenci podają różne szacunki: tygodnie vs miesiące, setki vs tysiące USD).
- Brak analizy prawnej dot. regulacji doradztwa inwestycyjnego w jurysdykcji autora.
- Brak jasności, czy "sentyment" ma dotyczyć konkretnych spółek, sektorów, czy szerszego rynku (klasa aktywów, geografia).

STATUS: CONTINUE