# idea-orch (Boardroom) — rada modeli nad pomysłem na aplikację

Rzucasz pomysł (`idea.md`), agenci oparci o różne modele toczą ustrukturyzowaną
debatę o koncepcji biznesowej, a na końcu dostajesz `concept.md` z werdyktem
**GO / NO-GO / PIVOT**.

## Instalacja

```bash
pip install -r requirements.txt
```

Klucz API (wystarczy jeden — OpenRouter jako agregator):

```powershell
$env:OPENROUTER_API_KEY = "sk-or-..."
```

Alternatywnie bezpośrednio u providerów: `ZHIPU_API_KEY`, `ANTHROPIC_API_KEY`,
`OPENAI_API_KEY` (wtedy usuń prefix `openrouter/` z nazw modeli w `config.yaml`).

## Użycie

```bash
python orchestrator.py --idea ../moj-pomysl/idea.md --name moj-pomysl
```

Wyniki lądują w `sessions/moj-pomysl/`:

```
sessions/moj-pomysl/
├── input/idea.md          # kopia pomysłu
├── 01_agenda.md           # agenda rady (architekt dyskusji)
├── round1/sceptic.md      # opinie agentów (równoległe, niezależne)
├── round1/_synthesis.md   # synteza moderatora: consensus, spory, status
├── round2/...             # kolejna runda (agenci widzą się nawzajem)
├── concept.md             # FINALNA KONCEPCJA + werdykt GO/NO-GO/PIVOT
└── run.log                # log wywołań: model, tokeny, czas, błędy
```

## Użycie jako skill / slash command (Claude Code / Cline)

Repo zawiera:
- skill `.claude/skills/boardroom/SKILL.md` — agent uruchomi debatę na życzenie,
- polecenie `/idea-orch` (`.claude/commands/idea-orch.md`) — debata jednym
  poleceniem z dowolnego folderu roboczego: `/idea-orch ./pomysl/idea.md`.

Instalacja globalna: skopiuj pliki do `~/.claude/skills/boardroom/` i
`~/.claude/commands/` (na tej maszynie kopie już tam są).
Dla autouzupełniania `/idea-orch` w Cline: skopiuj
`.clinerules/workflows/idea-orch.md` do projektu, w którym chcesz go używać.
Wymagany klucz: `OPENROUTER_API_KEY`.

## Przepływ

1. **Architekt dyskusji** (model mocny) — agenda wątków + pytania do rady.
2. **Runda 1** — Sceptyk (GLM), Visioner, Analityk — *równolegle i niezależnie*
   (bez groupthink).
3. **Moderator** (model mocny) — consensus, sporne pytania, luki; status
   `CONTINUE`/`CONVERGED` może skrócić debatę.
4. **Runda 2..N** — agenci odpowiadają na spory, widząc opinie pozostałych.
5. **Sędzia** (model mocny) — finalna koncepcja + werdykt.

## Konfiguracja

Wszystko w `config.yaml`: modele per rola (zmiana modelu = zmiana stringa),
liczba rund, limity kontekstu, temperatura. Prompty ról: `roles/*.md`,
prompty etapów: `prompts/*.md` — edytujesz bez dotykania kodu.

## Uwaga o modelach

Modele są ustawione przez OpenRouter (prefix `openrouter/...`, jeden klucz API).
Dostępne slug-i sprawdzisz na: https://openrouter.ai/models — wystarczy podmienić
string w `config.yaml`. Pełna lista providerów LiteLLM:
https://docs.litellm.ai/docs/providers

## Frontend na GitHub Pages

`docs/` zawiera statyczny UI: wpisz pomysł (tekst lub plik .md), wklej fine-grained
PAT (Contents RW + Actions W na to repo; trzymany w sessionStorage), kliknij
**Uruchom debatę** — frontend zapisze `queue/<slug>.md`, odpali workflow
`run-boardroom` (GitHub Action z Secret `OPENROUTER_API_KEY`) i wyświetli
`concept.md` z werdyktem GO/NO-GO/PIVOT.

Konfiguracja (jednorazowo):
1. Settings → Secrets and variables → Actions → `OPENROUTER_API_KEY`
2. Settings → Pages → Source: *Deploy from a branch* → `main` / `/docs`
3. Fine-grained PAT: https://github.com/settings/personal-access-tokens/new

Dwa profile konfiguracji:`n- ``config.yaml`` — pełne mapowanie modeli per rola (sonnet-5 / glm-5.3 / gpt-5.1 /`n  gpt-5-mini) — domyślny, zgodny z ``plan-idea-orch.md`` §6 (~$0.09/debatę),`n- ``config.flash.yaml`` — profil FLASH: wszystkie role na ``z-ai/glm-5.3-flash```n  (szybko, ~$0.02/debatę). GitHub Action ``run-boardroom`` używa właśnie tego`n  profilu (``--config config.flash.yaml``).`n`nSzczegóły planu implementacji: ``implementation_plan.md``.