## Ocena rynku
- Segment: aktywni inwestorzy detaliczni (DIY) aktywni na FinTwit/StockTwits/Reddit oraz użytkownicy brokerów mobilnych szukający kuracji treści. To wąska, ale angażująca nisza — nie obejmuje masy pasywnych inwestorów.
- Wielkość rynku (szacunek): w UE/UK może to być kilkaset tysięcy do ~1 mln aktywnych traderów gotowych eksperymentować z płatnymi narzędziami; globalnie kilka milionów. Realistyczny adresowalny rynek płacących początkowo: kilkanaście–kilkadziesiąt tys. użytkowników przy udanym produkcie.
- Implikacja: produkt musi silnie różnicować wartość (nie tylko „lepsze feedy”) lub celować w B2B (brokerzy, newslettery), by osiągnąć skalę.

## Konkurencja
- Bezpośredni/pośredni: TipRanks, Seeking Alpha, StockTwits, Dataminr, AlphaSense, Benzinga, RSS/Newslettery, darmowe społeczności FinTwit/Reddit.
- Różnica konkurencyjna wymagana: personalizacja rozumiana jako funkcjonalne dopasowanie do portfela + horyzont + reguł decyzyjnych (np. preferencja długiego trzymania, tolerancja drawdown) oraz aktywne moduły "higieny decyzji" (friction, analizy zachowań).
- Wniosek: deklaratywna przewaga („anty-hałas”) wymaga konkretnych, mierzalnych cech — np. redukcja liczby źródeł konsumowanych, zmniejszenie liczby impulsywnych transakcji o X%.

## Monetyzacja
- B2C subskrypcja 10–40 EUR wymaga jasnego USP. Bez udowodnionej predykcyjności sentymentu model jest ryzykowny.
- Alternatywy:
  - Freemium z płatnymi funkcjami personalizacji (integracja portfela, alerty, behavioral analytics).
  - B2B/white-label dla brokerów/portali — z wyraźnym value proposition: retencja klientów, mniejszy churn, lepsza angażacja.
- Czy wynika z wartości użytkownika? Tylko jeśli:
  - backtest pokaże wartość predykcyjną ORAZ/ALBO
  - da się udowodnić mierzalną redukcję czasu/hałasu lub spadek overtradingu (np. X% mniej transakcji, Y minut dziennie zaoszczędzone).
- Rekomendacja cenowa w MVP: testować niską stawkę (€5–10) + B2B piloty z płatnością za wdrożenie.

## Wykonalność MVP
- Minimalny POC (zalecane): RSS/API 3–5 wysokiej jakości źródeł, prosty rule-based sentiment scoring, brak LLM/scrapingu HTML. Czas: 4–8 tygodni dewelopersko-produkcyjnych.
- Backtest: konieczny protokół przed startem. Zakres: 6–12 miesięcy danych historycznych, metryki: hit rate, zwrot vs benchmark, drawdown, liczba dni bez sygnału. Szacunek kosztów i czasu:
  - Dane historyczne/API: 0–2000 EUR jednorazowo/mies. (zależnie od źródeł) — SZACUNEK.
  - Infrastruktura (serwery, DB, monitoring): ~200–1000 EUR/mies. — SZACUNEK.
  - Zespół do MVP: 1 full-stack dev + 1 data scientist (freelance) na 1–2 miesiące → koszt ~10–40 k EUR (zależnie od stawek) — SZACUNEK.
  - Koszty LLM znacząco rosną przy skali; uniknąć w MVP.
- Kluczowe zasoby: dostęp do historycznych danych, kompetencje DS (backtesting bez biasów), jasno zapisany protokół kill/continue.
- Ryzyka operacyjne i regulacyjne: unikać terminologii „rekomendacja”; early legal review (koszt kilkuset–kilku tys. EUR) zalecana przed komercjalizacją.

Odpowiedzi na pytania agendy / sporne kwestie
1. Backtest 6–12 mies. — jest warunkiem blokującym dla twierdzeń o alfa; równoległe projektowanie lekkiej architektury jest dopuszczalne, ale ciężka inwestycja w skalowanie powinna poczekać na wynik.
2. Próg sygnału i kryteria sukcesu — ustawić protokół przed testem. Propozycja: hit rate >55% na horyzoncie 3–5 dni i/lub zwrot netto vs. benchmark poprawiający Sharpe o >0.1; alternatywnie metryka „redukcji hałasu”: zmniejszenie liczby konsumowanych artykułów/sekcji o ≥30% z subiektywnym wzrostem satysfakcji (ankieta).
3. Dni bez sygnału — cisza/komunikat "brak okazji" (wartość UX). Nie wymuszać outputu.
4. Personalizacja vs filtry konkurencji — musi obejmować: integrację portfela, horyzont, reguły decyzyjne i behavioral friction; te elementy trzeba zdefiniować funkcjonalnie przed budową.
5. Kompetencje autora — brak danych; jeśli autor nie ma doświadczenia DS, konieczne partnerstwo lub zatrudnienie na etap backtestu (koszt i czas powyżej).