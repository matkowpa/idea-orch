## Zarzuty

1. **Ekonomia jednostkowa nie istnieje nawet przy sukcesie.** 10–40 EUR/mies. od wąskiej niszy FinTwit-owców, którzy z definicji są przyzwyczajeni do treści za 0 zł, to model, który wymaga tysięcy płacących, by pokryć koszty LLM, parserów i utrzymania źródeł danych. Policzmy brutalnie: 500 subskrybentów × 20 EUR = 10 tys. EUR/mies. przy koszty infrastruktury i danych (jeśli nie scrapujesz, płacisz za API) rzędu 2–5 tys. plus Twój czas. To hobby z fakturami, nie biznes. Nikt tego rachunku nie przedstawił.

2. **Backtest 6–12 miesięcy to koszt, którego nikt nie wycenił.** To nie jest "krok 2" — to 6–12 miesięcy Twojego życia przed pierwszym euro przychodu. Przy założeniu, że sentyment z publicznych portali jest spóźnionym echem (co rada już ustaliła), prawdopodobieństwo pozytywnego wyniku jest niskie. Oczekiwana wartość całego projektu = P(sentyment ma alpha) × wartość biznesu, a pierws czynnik jest prawdopodobnie <20%. Czy autor jest gotów spalić rok na loterię z takim kursem?

3. **"Redukcja szumu" jako wartość zastępcza jest niemierzalna — czyli niereklamowalna.** Jeśli backtest wyjdzie negatywny, pivot na "kurację" brzmi rozsądnie, ale jak sprzedasz "oszczędzasz 30 minut dziennie"? Nie masz metryki, nie masz benchmarku, a użytkownik nie zapłaci za coś, czego nie odczuwa w portfelu. To produkt, którego wartości nie da się udowodnić ani rynkowo, ani naukowo — najgorsza kombinacja.

4. **Zasoby autora są niewiadomą krytyczną, a wszyscy ją pomijają.** Pytanie 5 z agendy wisi bez odpowiedzi. Rzetelny backtest sentymentu to: dane historyczne (koszt), obsługa look-ahead bias, survivorship bias, stacjonarność sygnału. Samodzielnie robi to kompetentnie 1 na 20 programistów. Jeśli autor nie ma doświadczenia w data science, cała ścieżka "POC → backtest" jest fantazją.

5. **Pivot na B2B/white-label to ucieczka od problemu, nie rozwiązanie.** Brokerzy nie kupią sygnału bez zweryfikowanej wartości — przenosisz tylko barierę dowodową na klienta, który jest *bardziej* wymagający niż detal, nie mniej.

6. **Cisza w dni bez sygnału zabija retencję.** Odpowiedź na pytanie 3: użytkownik subskrypcyjny, który przez tydzień dostaje "brak okazji", anuluje subskrypcję. Wymuszony output generuje śmieci. To dylemat bez dobrego wyjścia w modelu B2C — i jest wbudowany w produkt, nie naprawialny.

## Co mnie przekonałoby

- **Rachunek kosztów na kartce**: konkretne liczby — koszt źródeł danych/API miesięcznie, koszt LLM na użytkownika, próg rentowności w liczbie subskrybentów. Bez tego nie ma o czym rozmawiać.
- **Backtest z góry zapisanym protokołem**: definicja sygnału, metryka (np. hit rate >55% na horyzoncie 5 dni vs. benchmark z korektą na ryzyko), próg kill/continue podpisane *przed* analizą. Jeśli autor potrafi to napisać sam — to też test kompetencji.
- **Odpowiedź na pytanie 5 wprost**: CV/zasoby autora. Jeśli brakuje kompetencji — partner z doświadczeniem ilościowym albo porzucenie projektu, nie samodzielna nauka na żywym pomysle.
- **Dowód, że ktoś zapłaci *zanim* powstanie produkt**: lista oczekujących z przedpłatą 3 miesięcy od 100 osób. To tani test, który zastępuje pół roku backtestu w kwestii popytu — choć nie w kwestii predykcyjności.

Moja pozycja: backtest jest blokujący (odp. na pytanie 1 — równoległe projektowanie architeektury to wydawanie zasobów bez fundamentu), ale *wcześniejszym* blokerem jest rachunek ekonomii i uczciwa ocena zasobów autora. Jeśli którykolwiek z tych trzech fundamentów (koszty, kompetencje, predykcyjność) nie stoi — projekt należy zamknąć, nie pivotować w nieskończoność.