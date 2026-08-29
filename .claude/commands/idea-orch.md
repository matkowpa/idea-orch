---
description: Odpal debatę boardroom nad pomysłem biznesowym (idea-orch)
argument-hint: [ścieżka-do-idea.md lub opis pomysłu]
---

# Boardroom — debata nad pomysłem biznesowym ($ARGUMENTS)

Uruchom orchestrator idea-orch (ścieżki absolutne, bieżący katalog roboczy nie ma znaczenia):

```
python "C:\Users\alusm\OneDrive\Dokumenty\Tata\projekty\idea-orch\orchestrator.py" --idea "<plik-pomysłu>" --name "<slug>"
```

Kroki:

1. Jeśli `$ARGUMENTS` wskazuje istniejący plik — użyj go jako `--idea`. Jeśli to opis pomysłu — zapisz go do tymczasowego `idea.md` (np. w cwd) i użyj jego ścieżki. Jeśli argument jest pusty — zapytaj użytkownika o pomysł.
2. Slug nazwij krótko (kebab-case) na podstawie tematu pomysłu.
3. Sprawdź, czy `OPENROUTER_API_KEY` jest ustawione; jeśli nie — poproś użytkownika o klucz, nie zgaduj.
4. Poinformuj użytkownika: wykonanie trwa kilka minut (10 wywołań LLM, ~$0.30).
5. Uruchom orchestrator i poczekaj na zakończenie.
6. Odczytaj `C:\Users\alusm\OneDrive\Dokumenty\Tata\projekty\idea-orch\sessions\<slug>\concept.md` i streść:
   werdykt (GO/NO-GO/PIVOT), kluczowe mocne strony, najpoważniejsze ryzyka,
   pytania pozostawione otwarte.
7. Pełne artefakty debaty (agenda, opinie per runda, syntezy) są w `sessions\<slug>\` — wskaż ścieżkę, nie wklejaj całości.

> UWAGA: ta kopia jest wersjonowana w repo. Kopia instalacyjna (używana jako
> polecenie `/idea-orch`) znajduje się w `~/.claude/commands/idea-orch.md` —
> po zmianach tutaj skopiuj ją tam.
