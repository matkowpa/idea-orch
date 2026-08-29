# Plan-idea-orch — założenia projektu i sposób realizacji (poprawiony)

> Wersja skorygowana względem `plan-idea-orch.md` po weryfikacji ze stanem repo
> (orchestrator.py, config.yaml, roles/, prompts/, test_smoke.py) i aktualną
> ofertą modeli na OpenRouter (stan: 2026-08-29). Zmiany względem oryginału są
> oznaczone w tekście; pełna lista na końcu dokumentu.

## 1. Cel projektu

**idea-orch (Boardroom)** to orchestrator dyskusji koncepcji biznesowych: użytkownik zgłasza pomysł na aplikację, a rada agentów — opartych o różne modele LLM o różnym potencjale — toczy ustrukturyzowaną debatę o sensie biznesowym pomysłu. Wynikiem jest `concept.md`: dopracowana koncepcja wraz z rejestrem ryzyk, nierozstrzygniętych kwestii i werdyktem **GO / NO-GO / PIVOT**.

Projekt jest pierwszą fazą szerszego pipeline'u: koncepcja → architektura → plan zadań → implementacja (fazy późniejsze, opcjonalne).

## 2. Kluczowe założenia projektowe

- **Rola ≠ model** — agent to para (prompt systemowy z `roles/*.md`) + model z `config.yaml`. Mapowanie model↔rola jest konfigurowalne jednym stringiem.
- **Różnorodność dostawców modeli jest częścią zabezpieczenia przed groupthink** — Sceptyk celowo używa innego dostawcy (Zhipu/GLM) niż reszta rady (Anthropic/OpenAI), żeby opinie różniły się także "z natury modelu", a nie tylko z promptu roli. *(doprecyzowanie — w oryginale ta zależność była tylko dorozumiana)*
- **Szyna komunikacji = pliki markdown** — każda opinia/synteza to osobny plik w `sessions/<idea>/`; pełna audytowalność, git-versioning, możliwość podglądu i wznowienia.
- **Równoległość i niezależność opinii w rundzie 1** — agenci nie widzą się nawzajem, żeby uniknąć groupthink; dopiero od rundy 2 otrzymują opinie pozostałych i syntezę moderatora.
- **Wczesne zatrzymanie debaty** — moderator kończy każdy etap linią `STATUS: CONTINUE|CONVERGED`; konwergencja przerywa pętlę rund przed limitem z configu.
- **Odporność na awarie** — retry ×3 z backoffem wykładniczym (`2**attempt`) na wywołanie modelu; awaria jednego agenta nie przerywa rundy (zapisywany jest marker `[ERROR]`).
- **Prompty poza kodem** — `roles/` i `prompts/` są edytowalne bez zmian w `orchestrator.py`.

## 3. Architektura pipeline'u

```
idea.md
  → [1] Architekt dyskusji (mocny model) → 01_agenda.md (wątki + pytania)
  → [2] Runda N — opinie RÓWNOLEGLE (asyncio.create_task):
        Sceptyk (GLM) / Visioner / Analityk → roundN/<agent>.md
  → [3] Moderator (mocny model) → roundN/_synthesis.md
        (consensus / spory jako pytania / luki / STATUS)
  → [4] pętla: jeśli CONTINUE i runda < limit → wróć do [2]
  → [5] Sędzia (mocny model) → concept.md (raport + werdykt)
```

*(korekta — krok [2] w kodzie używa `asyncio.create_task` per agent + `await` na słowniku tasków, nie bezpośrednio `asyncio.gather`; efekt identyczny — równoległość — ale nazwa API była nieścisła)*

Elementy towarzyszące: `run.log` (JSON per wywołanie: model, tokeny, czas, błędy), limit kontekstu `max_discussion_chars` (obcinanie historii opinii), `.gitignore` wykluczający `sessions/`, `__pycache__/`, `*.pyc`, `.env`.

## 4. Struktura repo

```
orchestrator.py     # cała logika (~240 linii, LiteLLM + asyncio)
config.yaml         # modele, agenci, rundy, limity, temperatura
roles/              # 6 promptów systemowych ról
prompts/            # 5 szablonów etapów (placeholdery {{...}})
test_smoke.py       # test E2E z atrapą LLM (bez kluczy API)
README.md, requirements.txt, .gitignore
```

*(korekta — `orchestrator.py` ma obecnie 237 linii, nie ~290; liczby ról/promptów w oryginale były poprawne)*

Stack: Python 3.12, LiteLLM (jedno API dla wszystkich providerów przez OpenRouter), PyYAML, asyncio.

## 5. Sposób realizacji (przyjęty i zweryfikowany)

1. Wspólny interfejs wywołań: `call_model()` (litellm.acompletion + retry + log) i `Boardroom.ask()` per agent.
2. Szablony promptów renderowane prostą substytucją `{{PLACEHOLDER}}` — zero zależności od silników template'ów.
3. Rundy opiniotwórcze jako `asyncio.create_task` per agent → niezależność + szybkość.
4. Stop-decyzja parsowana regexem `STATUS: ...` z syntezy moderatora.
5. **Dostęp do modeli przez OpenRouter** — jeden klucz API (`OPENROUTER_API_KEY`), prefix `openrouter/` w `config.yaml`; bezpośrednie klucze providerów jako alternatywa.
6. Testowanie: `test_smoke.py` monkeypatchuje `litellm.acompletion` i przeprowadza pełny pipeline (2 rundy, CONTINUE→CONVERGED, werdykt) — test przechodzi; zależności (`litellm==1.98.0`, `pyyaml`) zweryfikowane w bieżącym środowisku.

## 6. Modele — rekomendacja na dziś (OpenRouter, 2026-08-29)

*(sekcja nowa — w oryginale plan zakładał konkretne sluzi modeli bez daty weryfikacji; poniższe zastępuje domyślne wartości `config.yaml`)*

Modele w `config.yaml` (`glm-4.6`, `claude-sonnet-4.5`, `gpt-4o`, `gpt-4o-mini`) wciąż działają, ale nie są już bieżącą generacją danego dostawcy. Sprawdzony (WebFetch na `openrouter.ai`) aktualny stan:

| Rola w configu | Obecnie w repo | Rekomendacja (bieżąca generacja) | Uzasadnienie |
|---|---|---|---|
| `strong` (Architekt/Moderator/Sędzia) | `openrouter/anthropic/claude-sonnet-4.5` | `openrouter/anthropic/claude-sonnet-5` | bezpośredni następca, ten sam segment cena/jakość; `claude-opus-5` jako opcja "na bogato" dla Sędziego, jeśli jakość werdyktu > koszt |
| `glm` (Sceptyk) | `openrouter/z-ai/glm-4.6` | `openrouter/z-ai/glm-5.3` | następca generacyjny GLM; utrzymuje odrębność dostawcy (nie-zachodni model) jako źródło innego "punktu widzenia" |
| `vision` (Visioner) | `openrouter/openai/gpt-4o` | `openrouter/openai/gpt-5.1` | `gpt-4o` to już poprzednia generacja OpenAI; `gpt-5.1` to obecny, dobrze udokumentowany flagowiec średniej półki |
| `mid` (Analityk) | `openrouter/openai/gpt-4o-mini` | `openrouter/openai/gpt-5-mini` | bezpośredni odpowiednik "mini" w nowej generacji; tani, wystarczający do roli Analityka |

Uwagi:
- OpenRouter regularnie dodaje nowsze warianty (w trakcie sprawdzania widoczne były już np. `gpt-5.4-mini`, `gpt-5.6-*`, `glm-5.3-flash`) — **przed uruchomieniem produkcyjnym zweryfikuj aktualną listę i ceny na https://openrouter.ai/models**, bo to zmienia się szybciej niż ten dokument.
- `glm-5.3-flash` (ok. 20× tańszy niż `glm-5.3`) jest kandydatem na tryb `--dry-run` z pkt. 8, ale prawdopodobnie zbyt słaby na docelową rolę Sceptyka w realnej sesji.
- Zmiana modeli to edycja jednego bloku `models:` w `config.yaml` — zgodnie z założeniem "rola ≠ model" nie wymaga zmian w kodzie ani promptach.

## 7. Ekonomia przebiegu

Ceny OpenRouter dla modeli z §6 (per 1M tokenów, wejście/wyjście):

| Model (rola) | Input | Output |
|---|---|---|
| `claude-sonnet-5` (strong: Architekt/Moderator×N/Sędzia) | $2.00 | $10.00 |
| `glm-5.3` (Sceptyk) | $1.20 | $4.00 |
| `gpt-5.1` (Visioner) | $1.25 | $10.00 |
| `gpt-5-mini` (Analityk) | $0.25 | $2.00 |

Przy domyślnym configu (`rounds: 2`, `max_tokens: 2000`, `max_discussion_chars: 6000`) i typowych długościach odpowiedzi w tym pipeline:

| Scenariusz | Wywołań LLM | Koszt (orientacyjnie) |
|---|---|---|
| Konwergencja po rundzie 1 (`STATUS: CONVERGED`) | 6 | **~$0.05** |
| Pełne 2 rundy (limit z configu) | 10 | **~$0.09** |

- Główny koszt niesie `strong` (Claude Sonnet 5) — ~65% całości w wariancie pełnym — głównie przez wywołanie Sędziego: dostaje cały transkrypt debaty jako input i generuje najdłuższy output (`concept.md`).
- Wczesna konwergencja tnie koszt o ok. 40–45% (mniej wywołań `strong` i pominięta druga runda opinii).
- *(korekta — zastąpiono widełki „$0.25–0.35” / „$0.05–0.08” z oryginału, liczone dla nieaktualnego zestawu modeli, powyższym przeliczeniem dla modeli z §6; nadal to estymacja na podstawie typowych długości odpowiedzi, nie realnego przebiegu)*
- Docelowo: dokładne dane po realnym biegu z `run.log` (prompt/completion tokens per wywołanie) + skrypt sumujący koszt sesji wg aktualnego cennika OpenRouter (pkt. 8 roadmapy).

## 8. Roadmapa (kolejne kroki)

1. **Uruchomienie produkcyjne** — `OPENROUTER_API_KEY`, aktualizacja slug-ów modeli w `config.yaml` zgodnie z §6, pierwszy pełny bieg na prawdziwym pomyśle.
2. **Weryfikacja jakości debaty** — ocena, czy role dają zróżnicowane stanowiska; ewentualne strojenie promptów w `roles/`.
3. **Rozszerzenia krótkoterminowe:**
   - flaga `--dry-run` (wszyscy agenci na jednym tanim modelu, np. `glm-5.3-flash`),
   - `--resume` (wznowienie sesji z ostatniej rundy po awarii),
   - skrypt raportu kosztu z `run.log` (per aktualny cennik, nie stałe widełki w dokumentacji),
   - ewentualnie fallback modeli / warianty `:free` dla testów (dostępność wariantów `:free` zmienia się często — sprawdzać na bieżąco).
4. **Faza 2 (opcjonalna):** `--mode architecture` — ten sam szkielet, inne prompty: przekształcenie `concept.md` w architekturę techniczną; potem plan zadań dla agenta-kodera.

---

## Zmiany względem `plan-idea-orch.md`

1. §3: sprostowanie — kod używa `asyncio.create_task` per agent, nie `asyncio.gather` wprost.
2. §4: sprostowanie liczby linii `orchestrator.py` (237, nie ~290).
3. §2: dodano jawne wyjaśnienie *dlaczego* Sceptyk siedzi na innym dostawcy (GLM) — to było tylko dorozumiane w oryginale.
4. §5.6: doprecyzowano wersję `litellm` (potwierdzone `1.98.0` w środowisku) zamiast ogólnego "zainstalowane".
5. **Nowa sekcja §6** — aktualne (2026-08-29) rekomendacje modeli na OpenRouter per rola, w miejsce nieoznaczonych czasowo slug-ów z oryginału (`glm-4.6`, `claude-sonnet-4.5`, `gpt-4o`, `gpt-4o-mini` → `glm-5.3`, `claude-sonnet-5`, `gpt-5.1`, `gpt-5-mini`).
6. §7 (dawniej §6): usunięto konkretne widełki kosztowe („$0.25–0.35” itd.) — liczone dla nieaktualnego zestawu modeli/cen, wprowadzałyby w błąd bez przeliczenia.
7. §8 (dawniej §7): pkt. 1 zaktualizowany o odniesienie do nowej sekcji §6; pkt. 3 doprecyzowany o konkretną propozycję modelu do `--dry-run`.

`config.yaml` **nie został zmieniony** przez ten dokument — to tylko rekomendacja; wdrożenie nowych slug-ów to świadoma decyzja do podjęcia osobno (m.in. dlatego, że lista modeli na OpenRouter zmienia się szybciej niż ten plan).
