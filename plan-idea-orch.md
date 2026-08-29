# Plan-idea-orch — założenia projektu i sposób realizacji

## 1. Cel projektu

**idea-orch (Boardroom)** to orchestrator dyskusji koncepcji biznesowych: użytkownik zgłasza pomysł na aplikację, a rada agentów — opartych o różne modele LLM o różnym potencjale — toczy ustrukturyzowaną debatę o sensie biznesowym pomysłu. Wynikiem jest `concept.md`: dopracowana koncepcja wraz z rejestrem ryzyk, nierozstrzygniętych kwestii i werdyktem **GO / NO-GO / PIVOT**.

Projekt jest pierwszą fazą szerszego pipeline'u: koncepcja → architektura → plan zadań → implementacja (fazy późniejsze, opcjonalne).

## 2. Kluczowe założenia projektowe

- **Rola ≠ model** — agent to para (prompt systemowy z `roles/*.md`) + model z `config.yaml`. Mapowanie model↔rola jest konfigurowalne jednym stringiem (np. GLM jako Sceptyk, mocny model jako Moderator/Sędzia).
- **Szyna komunikacji = pliki markdown** — każda opinia/synteza to osobny plik w `sessions/<idea>/`; pełna audytowalność, git-versioning, możliwość podglądu i wznowienia.
- **Równoległość i niezależność opinii w rundzie 1** — agenci nie widzą się nawzajem, żeby uniknąć groupthink; dopiero od rundy 2 otrzymują opinie pozostałych i syntezę moderatora.
- **Wczesne zatrzymanie debaty** — moderator kończy każdy etap linią `STATUS: CONTINUE|CONVERGED`; konwergencja przerywa pętlę rund przed limitem z configu.
- **Odporność na awarie** — retry ×3 z backoffem na wywołanie modelu; awaria jednego agenta nie przerywa rundy (zapisywany jest marker `[ERROR]`).
- **Prompty poza kodem** — `roles/` i `prompts/` są edytowalne bez zmian w `orchestrator.py`.

## 3. Architektura pipeline'u

```
idea.md
  → [1] Architekt dyskusji (mocny model) → 01_agenda.md (wątki + pytania)
  → [2] Runda N — opinie RÓWNOLEGLE (asyncio.gather):
        Sceptyk (GLM) / Visioner / Analityk → roundN/<agent>.md
  → [3] Moderator (mocny model) → roundN/_synthesis.md
        (consensus / spory jako pytania / luki / STATUS)
  → [4] pętla: jeśli CONTINUE i runda < limit → wróć do [2]
  → [5] Sędzia (mocny model) → concept.md (raport + werdykt)
```

Elementy towarzyszące: `run.log` (JSON per wywołanie: model, tokeny, czas, błędy), limit kontekstu `max_discussion_chars` (obcinanie historii opinii), `.gitignore` wykluczający `sessions/` i `__pycache__`.

## 4. Struktura repo

```
orchestrator.py     # cała logika (~290 linii, LiteLLM + asyncio)
config.yaml         # modele, agenci, rundy, limity, temperatura
roles/              # 6 promptów systemowych ról
prompts/            # 5 szablonów etapów (placeholdery {{...}})
test_smoke.py       # test E2E z atrapą LLM (bez kluczy API)
README.md, requirements.txt, .gitignore
```

Stack: Python 3.12, LiteLLM (jedno API dla wszystkich providerów przez OpenRouter), PyYAML, asyncio.

## 5. Sposób realizacji (przyjęty i zweryfikowany)

1. Wspólny interfejs wywołań: `call_model()` (litellm.acompletion + retry + log) i `Boardroom.ask()` per agent.
2. Szablony promptów renderowane prostą substytucją `{{PLACEHOLDER}}` — zero zależności od silników template'ów.
3. Rundy opiniotwórcze jako `asyncio.create_task` per agent → niezależność + szybkość.
4. Stop-decyzja parsowana regexem `STATUS: ...` z syntezy moderatora.
5. **Dostęp do modeli przez OpenRouter** — jeden klucz API (`OPENROUTER_API_KEY`), prefix `openrouter/` w `config.yaml`; bezpośrednie klucze providerów jako alternatywa.
6. Testowanie: `test_smoke.py` monkeypatchuje `litellm.acompletion` i przeprowadza pełny pipeline (2 rundy, CONTINUE→CONVERGED, werdykt) — test przechodzi; zależności (`litellm 1.98.0`, `pyyaml`) zainstalowane.

## 6. Ekonomia przebiegu

- ~10 wywołań LLM na sesję (2 rundy), koszt szacowany **$0.25–0.35**.
- Główny koszt: mocny model (4 z 10 wywołań ≈ 55%); zamiana Moderatora na tańszy model obniża całość do ~$0.05–0.08.
- Wczesna konwergencja (`CONVERGED` po rundzie 1) tnie ~30% kosztu; koszt rośnie liniowo z liczbą rund.
- Dokładne dane po realnym biegu: `run.log` (prompt/completion tokens per wywołanie) — docelowo skrypt sumujący koszt sesji.

## 7. Roadmapa (kolejne kroki)

1. **Uruchomienie produkcyjne** — `OPENROUTER_API_KEY`, weryfikacja slug-ów modeli na https://openrouter.ai/models, pierwszy pełny bieg na prawdziwym pomyśle.
2. **Weryfikacja jakości debaty** — ocena, czy role dają zróżnicowane stanowiska; ewentualne strojenie promptów w `roles/`.
3. **Rozszerzenia krótkoterminowe:**
   - flaga `--dry-run` (wszyscy agenci na jednym tanim modelzie),
   - `--resume` (wznowienie sesji z ostatniej rundy po awarii),
   - skrypt raportu kosztu z `run.log`,
   - ewentualnie fallback modeli / warianty `:free` dla testów.
4. **Faza 2 (opcjonalna):** `--mode architecture` — ten sam szkielet, inne prompty: przekształcenie `concept.md` w architekturę techniczną; potem plan zadań dla agenta-kodera.
