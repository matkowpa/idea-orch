# Implementation Plan — Frontend idea-orch na GitHub Pages (wariant A)

## Overview
Statyczny frontend na GitHub Pages umozliwiajacy zgloszenie pomyslu na aplikacje (tekst lub plik) i uruchomienie debaty boardroom przez GitHub Action; wynik (sessions/<slug>/concept.md) jest pollowany i renderowany w UI. Profil modeli: szybki GLM flash (z-ai/glm-4.5-flash) na wszystkich rolach.

## Types / kontrakty
- Frontend -> GitHub API:
  - PUT /repos/matkowpa/idea-orch/contents/queue/<slug>.md  (message, content=base64(pomysl), sha jesli plik istnieje)
  - POST /repos/matkowpa/idea-orch/actions/workflows/run-boardroom.yml/dispatches ({"ref":"main"})
- Polling: GET https://raw.githubusercontent.com/matkowpa/idea-orch/main/sessions/<slug>/concept.md?t=<ts> — 200 = gotowe.
- Workflow inputs: slug (string, kebab-case).

## Files
- config.yaml [MODIFY]: models -> flash: openrouter/z-ai/glm-4.5-flash; wszystkie agenci model: flash; zakomentowany strong (opcja glebszej debaty).
- .github/workflows/run-boardroom.yml [NEW]: workflow_dispatch input slug; jobs.boardroom (ubuntu-latest, permissions contents:write): checkout@v4, setup-python@v5 (3.12), pip install -r requirements.txt, run: python orchestrator.py --idea "queue/$SLUG.md" --name "$SLUG" (env SLUG, OPENROUTER_API_KEY=secrets.OPENROUTER_API_KEY), commit: git add -f sessions/$SLUG; commit+push jako boardroom-bot.
- docs/index.html [NEW]: jednostronicowy UI — pola (slug, pomysl textarea, upload pliku .md, PAT password + zapis do sessionStorage), przycisk Uruchom debate, status, obszar wyniku, link do artefaktow.
- docs/app.js [NEW]: GitHub API, slugify (kebab-case, sanitizacja), dispatch, polling co 10 s (timeout 10 min), render markdown (marked.js CDN).
- docs/style.css [NEW]: minimalny czytelny styl.
- README.md [MODIFY]: sekcja Frontend GitHub Pages (Secrets + Pages + PAT).

## Functions (app.js)
- slugify(text) -> kebab-case
- saveIdea(slug, content) -> PUT contents API (base64; 422 => GET sha => PUT ponownie)
- dispatchRun(slug) -> POST workflow dispatch
- pollResult(slug, onDone) -> interval 10 s, fetch raw concept.md, 404 => czekaj, 200 => render
- renderMarkdown(text) -> marked.parse
- upload pliku (FileReader -> textarea), PAT w sessionStorage (klucz gh_pat), walidacja pol

## Dependencies
- marked.js z CDN — zero buildu, zero node_modules.
- Backend: istniejace requirements.txt instalowane w Action.
- GitHub Secret: OPENROUTER_API_KEY (do ustawienia recznie przez wlasciciela).

## Testing
- Unitarnie: slugify (polskie znaki), sanitizacja slug.
- E2E lokalne: python test_smoke.py.
- E2E prawdziwe: wpisac pomysl testowy w UI -> obserwowac Action log -> UI pokazuje concept.md; weryfikacja commitow sessions/<slug>.
- Edge: brak Secret => Action failuje => UI po timeoutie pokazuje link do logu Action.

## Implementation Order
1. config.yaml -> profil flash (+ smoke-test dla pewnosci parsowania)
2. .github/workflows/run-boardroom.yml
3. docs/index.html + style.css + app.js
4. README.md -> sekcja Frontend + instrukcja konfiguracji
5. git add/commit/push (main)
6. Konfiguracja reczna: (a) Settings->Secrets->Actions->OPENROUTER_API_KEY, (b) Settings->Pages->Deploy from branch: main /docs, (c) fine-grained PAT (Contents: RW, Actions: W) wklejone w UI
7. Test E2E na zywo.

## Uwagi / decyzje
- Repo publiczne = wyniki debat widoczne publicznie (zaakceptowane).
- PAT w sessionStorage, nigdzie nie commitowany.
- queue/<slug>.md zapisywany przez frontend (historia pomyslow); sessions commitowane z -f (ominiecie .gitignore).
- Koszt na glm-4.5-flash ~$0.01-0.03/przebieg; czas ~1-2 min.
- Trade-off: flash = slabsza synteza niz strong (swiadomy, dla szybkosci).
