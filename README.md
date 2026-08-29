# idea-orch (Boardroom) — rada modeli nad pomysłem na aplikację

Rzucasz pomysł (`idea.md`), agenci oparci o różne modele LLM toczą ustrukturyzowaną
debatę o koncepcji biznesowej, a na końcu dostajesz `concept.md` z werdyktem
**GO / NO-GO / PIVOT** i raportem kosztów sesji.

Założenia i pełny plan: **`plan-idea-orch.md`**. Plan implementacji frontendu:
`implementation_plan.md`.

## Instalacja

```bash
pip install -r requirements.txt
```

Klucz API (wystarczy jeden — OpenRouter jako agregator):

```powershell
$env:OPENROUTER_API_KEY = "sk-or-..."
```

Alternatywnie bezpośrednio u providerów: `ZHIPU_API_KEY`, `ANTHROPIC_API_KEY`,
`OPENAI_API_KEY` (wtedy usuń prefix `openrouter/` z nazw modeli w configu).

## Użycie

```bash
python orchestrator.py --idea ../moj-pomysl/idea.md --name moj-pomysl
```

Opcje:
- `--config config.flash.yaml` — profil FLASH (wszyscy agenci na jednym tanim,
  szybkim modelu — tryb „szybkiego szkicu" / dry-run),
- `--config` przyjmuje dowolny plik konfiguracji.

Wyniki lądują w `sessions/moj-pomysl/`:

```text
sessions/moj-pomysl/
├── input/idea.md          # kopia pomysłu
├── 01_agenda.md           # agenda rady (architekt dyskusji)
├── round1/sceptic.md      # opinie agentów (równoległe, niezależne)
├── round1/_synthesis.md   # synteza moderatora: consensus, spory, status
├── round2/...             # kolejna runda (agenci widzą się nawzajem)
├── concept.md             # FINALNA KONCEPCJA + werdykt + raport kosztów na końcu
├── cost_report.md         # ten sam raport kosztów jako osobny plik
└── run.log                # log wywołań: model, tokeny, czas, błędy (JSONL)
```

Raport kosztów na końcu `concept.md` liczy koszt per model z realnych liczb
z `run.log`; ceny pobierane z API OpenRouter (cache: `pricing_cache.json`,
fallback: cennik z planu §7).

## Przepływ

1. **Architekt dyskusji** (model mocny) — agenda wątków + pytania do rady.
2. **Runda 1** — Sceptyk (GLM — celowo inny dostawca niż reszta, anti-groupthink),
   Visioner, Analityk — *równolegle i niezależnie*.
3. **Moderator** (model mocny) — consensus, sporne pytania, luki; status
   `CONTINUE`/`CONVERGED` może skrócić debatę.
4. **Runda 2..N** — agenci odpowiadają na spory, widząc opinie pozostałych.
5. **Sędzia** (model mocny) — finalna koncepcja + werdykt.
6. **Raport kosztów** — dopisywany na końcu `concept.md`.

Odporność: retry ×3 z backoffem na wywołanie; pusta treść od modelu reasoning
jest traktowana jak awaria (też retry); awaria jednego agenta nie przerywa rundy.

## Konfiguracja — dwa profile

| Plik | Profile | Koszt/bieg |
|---|---|---|
| `config.yaml` (domyślny) | pełne mapowanie per rola: `strong`=claude-sonnet-5 (Architekt/Moderator/Sędzia), `glm`=glm-5.3 (Sceptyk), `vision`=gpt-5.1 (Visioner), `mid`=gpt-5-mini (Analityk) — zgodnie z `plan-idea-orch.md` §6 | ~$0.09 |
| `config.flash.yaml` | FLASH: wszystkie role na `z-ai/glm-5.3-flash` — szybki szkic/dry-run | ~$0.02 |

Wspólne ustawienia: `rounds: 2`, `max_tokens: 4000`, `max_discussion_chars: 6000`,
`temperature: 0.7`, `reasoning_effort: low` (modele reasoning GLM — ogranicza
budżet rozumowania, żeby treść nie została „zjedzona"; przesyłane przez
`extra_body` w formacie OpenRouter).

Zmiana modelu = zmiana stringa w bloku `models:`. Prompty ról: `roles/*.md`,
prompty etapów: `prompts/*.md` — edytujesz bez dotykania kodu.
Slug-i modeli sprawdzisz na: https://openrouter.ai/models

## Frontend na GitHub Pages

**Strona: https://matkowpa.github.io/idea-orch/** — wpisz pomysł (tekst lub plik .md), wklej fine-grained
PAT (Contents RW + Actions W na to repo; trzymany w sessionStorage), kliknij
**Uruchom debatę** — frontend zapisze `queue/<slug>.md`, odpali workflow
`run-boardroom` (GitHub Action z Secret `OPENROUTER_API_KEY`) i wyświetli
`concept.md` z werdyktem GO/NO-GO/PIVOT i raportem kosztów.

Action uruchamia debatę na **domyślnym** `config.yaml` (pełne mapowanie ról).
Konfiguracja (jednorazowo):
1. Settings → Secrets and variables → Actions → `OPENROUTER_API_KEY`
2. Settings → Pages → Source: *Deploy from a branch* → `main` / `/docs`
3. Fine-grained PAT: https://github.com/settings/personal-access-tokens/new

## Użycie jako skill / slash command (Claude Code / Cline)

Repo zawiera:
- polecenie `/idea-orch` (`.claude/commands/idea-orch.md`) — debata jednym
  poleceniem z dowolnego folderu roboczego: `/idea-orch ./pomysl/idea.md`,
- skill `.claude/skills/boardroom/SKILL.md` — agent uruchomi debatę na życzenie,
- workflow Cline: `.clinerules/workflows/idea-orch.md` (autouzupełnianie `/`
  w Cline; globalnie: `~/.clinerules/workflows/`).

Instalacja globalna Claude Code: skopiuj do `~/.claude/commands/` (i opcjonalnie
`~/.claude/skills/boardroom/`). Wymagany klucz: `OPENROUTER_API_KEY`.

## Testy

```bash
python test_smoke.py   # pełny pipeline na atrapie LLM, bez kluczy API
python cost_report.py sessions/<slug>   # raport kosztów istniejącej sesji
```
