# Koncepcja biznesowa: "Bestiariusz Emocji"

## 1. Koncepcja (2-3 zdania)
Aplikacja mobilna, w której użytkownik generuje potworka odzwierciedlającego swój nastrój, wyładowuje na nim emocje, a następnie uspokaja go poprzez technikę regulacji emocji, zapisując go w osobistym bestiariuszu. Cel: połączenie natychmiastowej "wentylacji" z refleksją terapeutyczną w gamifikowanej formie.

## 2. Problem i grupa docelowa
Problem: potrzeba szybkiego narzędzia do rozładowania złości w momencie jej wystąpienia. Rada (visionary, analyst) rekomenduje wiążącą decyzję: **nastolatki 13-18, kanał B2B2C przez szkoły/psychologów szkolnych** — jako beachhead z zarządzalnym ryzykiem reputacyjnym i realną wartością terapeutyczną. Sceptic zgłasza zastrzeżenie: to najdroższa, nie najtańsza grupa (RODO, długi cykl sprzedaży B2B), i decyzja ta nie została poparta ani jedną rozmową z realnym nabywcą.

## 3. Model monetyzacji
Freemium (B2C) uzupełniony licencjami instytucjonalnymi (B2B2C: szkoły, poradnie, programy wellbeing) — wykluczona monetyzacja "eskalacji agresji". Model warunkowo sensowny, ale nierozwiązany: nikt nie oszacował CAC w kanale szkolnym (cykl 6-18 miesięcy, sezonowość budżetów, wielu decydentów) — ryzyko wskazane przez sceptica, że koszt akwizycji przewyższy przychód z licencji.

## 4. Konkurencja i przewaga
Konkurencja pośrednia: Calm, Headspace, Woebot, Daylio. Przewaga narracyjna ("agresja → transformacja → kolekcjonowanie") jest unikalna koncepcyjnie, ale — jak trafnie punktuje sceptic — jest to różnicowanie kosmetyczne, nieudowodnione empirycznie, wobec graczy z większym zaufaniem i budżetem marketingowym. Plan B (dziennik emocji bez agresji) traci ten wyróżnik i wchodzi na przetłoczony rynek Daylio/How We Feel bez przewagi.

## 5. Główne ryzyka (z atrybucją)
- **Fundament naukowy sporny/obalony** — hipoteza katharsis może utrwalać agresję, nie redukować (sceptic, za Bushmanem; potwierdzone przez analyst).
- **Perwersyjna metryka sukcesu** — bestiariusz nagradza częstotliwość złości (sceptic, przyjęte przez wszystkich jako błąd do naprawy).
- **Ryzyko reputacyjne/App Store** — symboliczna przemoc wobec istoty może być odrzucona w review lub wywołać krytykę medialną (sceptic).
- **Odwrócona kolejność walidacji** — rada testuje mechanikę psychologiczną, zanim potwierdzi istnienie płacącego klienta; sceptic słusznie wskazuje, że 3-5 rozmów z psychologami szkolnymi (koszt: telefon) daje więcej informacji biznesowych niż całe RCT.
- **RODO/compliance dla <16** — potencjalny deal-breaker kosztowy, nieoszacowany (sceptic, moderator).
- **Niedostateczna moc pilotażu** — N=60-90 przy proponowanym budżecie może dać nierozstrzygający "szum" zamiast odpowiedzi — "teatr walidacji" (sceptic).
- **Brak dyscypliny projektowej** — rozbieżność wycen (15k-150k zł/USD), brak jednego podpisanego progu sukcesu, brak wskazanego PI z nazwiskiem (sceptic, moderator).
- **Faza 1 może zdominować użycie**, degradując produkt do "punch simulator" (sceptic).

## 6. Nierozstrzygnięte kwestie
- Kolejność działań walidacyjnych: najpierw klient i prawnik (sceptic) vs. równolegle z pilotażem naukowym (analyst/visionary) — **rozstrzygam poniżej**.
- Jeden, podpisany próg sukcesu pilotażu i wskazanie realnego PI.
- Formalny status planu B: nowy projekt czy kontynuacja wizji — nierozstrzygnięte, wymaga osobnej decyzji biznesowej.
- Zamknięty budżet i deadline walidacji (15k/8 tyg. vs 20-40k/3-4 mies.).
- Desk research wielkości rynku B2B2C i CAC w kanale szkolnym.

## 7. Werdykt: PIVOT

**Uzasadnienie:** Koncepcja ma ciekawy wyróżnik narracyjny, ale opiera się na naukowo spornym fundamencie i — co ważniejsze — dwie pełne rundy dyskusji nie potwierdziły nawet istnienia płacącego klienta. Przyjmuję argument sceptica jako rozstrzygający w sporze o kolejność: **testowanie hipotezy psychologicznej przed hipotezą rynkową to błąd sekwencji**, który powtarzałby się w mniejszej skali nawet po pilotażu.

Rekomendowana kolejność (rozstrzygnięcie sporu z Rundy 2):
1. **Tydzień 1-2:** 3-5 rozmów sprzedażowych z psychologami szkolnymi/dyrektorami + pisemna opinia prawnika o RODO/DPIA dla <16 (koszt łączny: ~3-5k zł). Brak zainteresowania zakupowego = koniec projektu, bez dalszych kosztów.
2. **Tylko jeśli krok 1 pozytywny:** pilotaż naukowy z grupami porównawczymi (mechanika vs oddech vs kontrola), z jednym podpisanym progiem sukcesu i wskazanym PI klinicznym. Budżet zamknięty: max 15-20k zł, 8 tygodni — akceptuję niższy, zdyscyplinowany wariant sceptica jako bezpieczniejszy wobec ryzyka "teatru walidacji".
3. Plan B (dziennik emocji bez agresji) traktować jawnie jako **odrębny projekt** z własną analizą konkurencji — nie jako łagodniejszą wersję tej samej wizji.

Budowa pełnego MVP przed tymi krokami byłaby najdroższym możliwym sposobem sprawdzenia hipotezy, która może zderzyć się z brakiem rynku, zanim zderzy się z brakiem dowodu naukowego.

---

# Raport kosztów sesji

_2026-08-29 11:30 UTC_

| Model | Wywołania | Tokeny in | Tokeny out | Koszt (USD) |
|---|---|---|---|---|
| `openrouter/anthropic/claude-sonnet-5` | 4 | 35,450 | 6,605 | $0.1370 |
| `openrouter/openai/gpt-5-mini` | 2 | 8,679 | 2,868 | $0.0079 |
| `openrouter/openai/gpt-5.1` | 2 | 8,641 | 3,407 | $0.0449 |
| `openrouter/z-ai/glm-5.3` | 2 | 8,949 | 2,387 | $0.0203 |

**RAZEM: $0.2100**
