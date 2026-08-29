# Koncepcja biznesowa: Personalizowany Asystent Sentymentu Inwestycyjnego

## 1. Koncepcja
Aplikacja monitorująca serwisy inwestycyjne i generująca skondensowane, spersonalizowane sygnały/informacje dla inwestorów detalicznych, z ambicją redukcji szumu informacyjnego (nie predykcji rynku). W obecnej formie łączy niezweryfikowaną obietnicę wartości predykcyjnej z modelem subskrypcyjnym B2C.

## 2. Problem i grupa docelowa
Deklarowany problem: przeciążenie informacyjne aktywnych inwestorów DIY (FinTwit/StockTwits/Reddit). Rada (sceptic) podała w wątpliwość, czy realnym problemem nie jest raczej brak dyscypliny decyzyjnej niż dostęp do informacji — szybsze sygnały mogą ten problem pogłębiać. Grupa docelowa jest wąska (nisza aktywnych traderów, nie inwestorów pasywnych) i przyzwyczajona do darmowych treści, co utrudnia konwersję na płatny model.

## 3. Model monetyzacji
Subskrypcja B2C 10–40 EUR/mies., freemium, opcjonalnie B2B/white-label. Analyst wskazał, że przy konwersji freemium→paid na poziomie 1–5% i konkurencji „za 0 zł” próg rentowności wymaga tysięcy płacących użytkowników — rachunku tego nikt nie przedstawił (sceptic). Monetyzacja jest uzasadniona wyłącznie po: (a) pozytywnym backteście LUB (b) dowodzie mierzalnej redukcji czasu/hałasu, potwierdzonym gotowością do płacenia (np. przedpłaty).

## 4. Konkurencja i przewaga
Silna konkurencja (TipRanks, Seeking Alpha, StockTwits, Dataminr, AlphaSense) plus darmowe alternatywy. Deklarowana przewaga „personalizacja + limit sygnałów” jest niezdefiniowana funkcjonalnie i niezweryfikowana wobec istniejących filtrów. Visionary zaproponował konkretyzację (profil: portfel × horyzont × tolerancja ryzyka × styl), ale to wciąż projekt na papierze, nie zweryfikowany rynkowo.

## 5. Główne ryzyka (z atrybucją)
- **Brak dowodu wartości predykcyjnej sentymentu** — może być spóźnionym echem rynku, podatnym na manipulację (sceptic).
- **Brak rachunku ekonomii jednostkowej** — nikt nie przedstawił kosztów danych/API/LLM vs próg rentowności; sceptic szacuje, że nawet sukces subskrypcyjny to „hobby z fakturami” (sceptic).
- **Niewiadoma krytyczna: kompetencje i zasoby autora** (DS, budżet 10–40k EUR na backtest/partnera) — nierozstrzygnięta przez dwie rundy dyskusji, mimo wielokrotnych pytań (sceptic, analyst).
- **Sprzeczność produktowa "1 rekomendacja dziennie"** i ryzyko churnu przy ciszy w dni bez sygnału w modelu subskrypcyjnym B2C (sceptic, potwierdzone przez visionary jako wymagające przeprojektowania).
- **Niemierzalność "redukcji szumu/dyscypliny"** bez kosztownego badania behawioralnego — sceptic nazywa to „wartością niereklamowalną”; visionary proponuje operacjonalizację (czas w feedach, liczba transakcji), ale koszt pomiaru pozostaje nierozwiązany.
- **Piramida założeń skalowania** — plany B2B/community/profile inwestora (visionary) budowane bez zweryfikowanego fundamentu; sceptic ocenia to jako „przesunięcie fantazji w czasie”.
- **Ryzyko regulacyjne (MiFID II)** — pełny konsensus rady, że słowo „rekomendacja” i architektura produktu grożą wpadnięciem w regulowane doradztwo inwestycyjne.
- **Ryzyko operacyjne** — koszty utrzymania scraperów/parserów, ToS, koszty LLM niedoszacowane w pierwotnej koncepcji (analyst, sceptic).

## 6. Nierozstrzygnięte kwestie
- Profil autora: doświadczenie DS, budżet, czas — pytanie zadawane dwukrotnie, bez odpowiedzi.
- Konkretny rachunek jednostkowy (koszt/użytkownika, próg rentowności).
- Czy "higiena informacyjna/dyscyplina" (tor B visionary) jest samodzielnym biznesem, czy tym samym zakładem w nowym opakowaniu (spór sceptic vs visionary nierozstrzygnięty).
- Czy da się tanio i wiarygodnie zmierzyć „redukcję szumu” bez kosztownego badania behawioralnego.
- Spisany, zatwierdzony protokół kill-switch backtestu (propozycje różnią się między agentami: hit rate 55% vs information ratio >0,3 vs 30-50% redukcji czasu).
- Dowód popytu (przedpłaty, landing page) — niewykonany.

## 7. Werdykt: PIVOT (warunkowy, z realną groźbą NO-GO)

**Uzasadnienie:** Rada osiągnęła pełny konsensus, że projekt w obecnej formie nie ma zweryfikowanego fundamentu — backtest jest blokujący, a mimo dwóch rund dyskusji kluczowe pytanie o zasoby/kompetencje autora pozostało bez odpowiedzi. To jest sygnał ostrzegawczy: jeśli po dwóch rundach rada nie może wyegzekwować tej podstawowej informacji, ryzyko jest wysokie, że projekt nie przejdzie nawet do fazy POC.

Rekomendowany pivot z „generatora rekomendacji” na „narzędzie kuracji/higieny informacyjnej” pozycjonowane jako analiza, nie doradztwo, ale **obwarowany trzema równorzędnymi, blokującymi warunkami wstępnymi** (sceptic trafnie wskazał, że to niezależne od siebie blokery – każdy samodzielnie może zamknąć projekt):

1. **Rachunek jednostkowy na kartce** (koszt danych/API/LLM, próg rentowności w subskrybentach) — do wykonania w dniach, nie miesiącach.
2. **Wprost odpowiedź o zasobach autora** (DS, budżet, czas) — determinuje, czy ścieżka backtestu jest realna samodzielnie, wymaga partnera, czy projekt należy zamknąć.
3. **Tani test popytu** (100 przedpłat/landing page) — niezależny od wyniku backtestu, weryfikujący, czy ktokolwiek zapłaci.

Dopiero po pozytywnym przejściu tych trzech filtrów: POC (3-5 źródeł, rule-based, bez LLM/scrapingu) → backtest 6-12 mies. z protokołem kill/continue spisanym z góry → decyzja o komercjalizacji z naciskiem na wariant „higiena/dyscyplina” (mniej ryzykowny regulacyjnie i logicznie bardziej odporny na negatywny wynik backtestu niż czysta obietnica alfa).

Jeśli którykolwiek z trzech warunków wstępnych zawiedzie (brak rentownej ekonomii, brak kompetencji/partnera, brak popytu) — werdykt zmienia się na **NO-GO**. Budowanie architektury skalowania (B2B, community, „standard profilu inwestora”) przed tymi walidacjami jest przedwczesne i nie powinno pochłaniać zasobów.

---

# Raport kosztów sesji

_2026-08-29 12:03 UTC_

| Model | Wywołania | Tokeny in | Tokeny out | Koszt (USD) |
|---|---|---|---|---|
| `openrouter/anthropic/claude-sonnet-5` | 4 | 35,380 | 6,692 | $0.1377 |
| `openrouter/openai/gpt-5-mini` | 2 | 7,951 | 2,737 | $0.0075 |
| `openrouter/openai/gpt-5.1` | 2 | 7,913 | 3,547 | $0.0454 |
| `openrouter/z-ai/glm-5.3` | 2 | 8,238 | 2,597 | $0.0203 |

**RAZEM: $0.2108**
