## Ocena rynku
- Segment: aplikacje do regulacji emocji / zdrowia psychicznego + casualne gry „antystresowe”. Trafia głównie do dwóch segmentów: młodzi dorośli (18–35) z wysokim stresem i nastolatki/early teens szukające szybkich kanałów rozładowania. Potencjalnie też rodzice nastolatków i terapeuci szukający narzędzia do ćwiczeń emocjonalnych.
- Wielkość rynku: rynek aplikacji zdrowia psychicznego i wellbeing jest duży i rosnący globalnie (miliardy USD). Realnie osiągalny podsegment (antystres/gamified emotional regulation) to nisza w obrębie tego rynku — możliwość zdobycia kilkudziesięciu tysięk–setek tysięcy aktywnych użytkowników w krajach docelowych w ciągu 1–2 lat przy umiarkowanym budżecie marketingowym (szacunek).
- Popyt: istnieje potrzeba szybkich mechanizmów rozładowania emocji, ale wielu użytkowników preferuje sprawdzone metody (sport, medytacja). Produkt musi jasno komunikować dodatkową wartość (bezpieczne wyładowanie + śledzenie postępów).

## Konkurencja
- Bezpośrednie/pośrednie: aplikacje antystresowe i casual games (e.g., Virtual punchbag / stress relief simulators), „angry typing” websites, aplikacje do mood tracking (Daylio), gry relaksacyjne (Toca Boca dla młodszych).
- Silni gracze w sąsiednich obszarach: Calm, Headspace, Moodpath, Woebot (AI terapeuta) — oferują regulację nastroju, tracking i psychologiczne ścieżki.
- Różnica produktu: mechanika „agresja → transformacja → kolekcjonowanie” jest unikalna narracyjnie, ale konkurencja ma większe zaufanie/rozpoznawalność.

## Monetyzacja
- Model naturalny: freemium. Darmowa podstawowa sesja + płatne rozszerzenia:
  - Skins / potworki premium i animacje (mikropłatności).
  - Subskrypcja PRO: zaawansowane statystyki nastroju, historie potworków, spersonalizowane sesje, integracja z terapeutą / eksport raportów.
  - Jednorazowe pakiety „terapeutyczne” z zaplanowanymi ścieżkami rozmów (paywall).
- Ocena: monetyzacja wynika z wartości (kolekcjonowanie, personalizacja, raporty) jeśli retention jest wysoka. Trzeba uważać, by nie sprzedawać „bardziej brutalnych” funkcji jako premium (etyka, reputacja).

## Wykonalność MVP
- Minimalny zakres (zalecane): 2D potworek generator (parametry nastroju → wygląd/agresywność), prosta mechanika wyładowania (klikanie, swipe, stylizowany „punch”), proste uspokojenie: scripted dialogy / wybory użytkownika prowadzące do transformacji, podstawowy bestiariusz + prosty mood tracker (liczba uspokojonych potworków).
- Zasoby i koszty (szacunek):
  - Zespół: 1 PM/product, 1–2 devowie (mobile), 1–2 UI/animator, 1 UX/psycholog konsultant, 1 QA, marketing początkowy.
  - Czas: 3–4 miesiące MVP.
  - Koszty: zależne od lokalizacji, ale budżet początkowy na MVP to rząd wielkości 50–150k USD (szacunek) przy outsourcingu/małym zespole.
- Technologia: Unity/React Native dla cross-platform; backend prosty do user data + analytics. AI (NLP) do dialogów może być etapem 2 — MVP używa skryptów.

Odpowiedzi na pytania z agendy
1. Dowody, że „bicie potworka” redukuje złość? Badania wskazują sprzeczne wyniki — katharsis nie zawsze redukuje agresję; czasami wzmacnia. Konieczne testy z użytkownikami (A/B) i współpraca z psychologiem przed skalowaniem.
2. Zabezpieczenia przed niewłaściwym użyciem: age-gating, ograniczenia częstotliwości sesji, in-app disclaimer, onboarding edukujący, wykrywanie wzorca intensywnego użycia -> proponowanie pomocy/zasobów, opcja zgłoszenia treści, moderacja jeśli jest user-generated content.
3. Minimalny zestaw funkcji do walidacji hipotezy: 1) prosty potworek + mechanika wyładowania, 2) możliwość uspokojenia z zapisem w bestiariuszu, 3) podstawowy mood tracker i krótkie ankiety pre/post sesja (pomiar subiektywnego nastroju). Testy z 100–300 użytkownikami do weryfikacji efektu.
4. Różnica od istniejących aplikacji: narracyjna pętla (agresja→transformacja→kolekcjonowanie) i gamifikacja emocjonalnej pracy. Musi być jednak udowodniona skuteczność i nie-infantylność UX dla dorosłych.
5. Model monetyzacji a etyka: unikać płatnych opcji „bardziej brutalnych” — zamiast tego monetyzować personalizację, raporty, integracje z terapią i estetyczne skiny. Etycznie problematyczne treści powinny być darmowe/ograniczone.

Rekomendacja: zbudować szybkie MVP skupione na testach behawioralnych z udziałem psychologa, zebrać dane pre/post sesji i feedback użytkowników przed inwestycją w AI/dużą bibliotekę contentu.