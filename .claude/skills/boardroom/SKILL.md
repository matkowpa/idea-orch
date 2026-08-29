---
name: boardroom
description: >-
  Rada agentów LLM oceniająca pomysł biznesowy aplikacji. Użyj, gdy użytkownik
  przedstawi lub wskaże plik z pomysłem na aplikację i zechce oceny koncepcji
  biznesowej / werdyktu GO-NO-GO-PIVOT. Wymaga OPENROUTER_API_KEY.
---

# Boardroom — debata nad pomysłem biznesowym

Uruchom orchestrator (ścieżki absolutne, bieżący katalog roboczy nie ma znaczenia):

```
python "C:\Users\alusm\OneDrive\Dokumenty\Tata\projekty\idea-orch\orchestrator.py" --idea "<ścieżka-do-idea.md>" --name "<slug>"
```

Zasady:

- Jeśli `OPENROUTER_API_KEY` nie jest ustawione — poproś użytkownika o klucz, nie zgaduj.
- Slug nazwij krótko (kebab-case) na podstawie tematu pomysłu.
- Wykonanie trwa kilka minut (10 wywołań LLM, ~$0.30) — poinformuj użytkownika.
- Po zakończeniu odczytaj `C:\Users\alusm\OneDrive\Dokumenty\Tata\projekty\idea-orch\sessions\<slug>\concept.md` i streść:
  werdykt (GO/NO-GO/PIVOT), kluczowe mocne strony, najpoważniejsze ryzyka,
  pytania pozostawione otwarte.
- Pełne artefakty debaty (agenda, opinie per runda, syntezy) są w
  `sessions\<slug>\` — wskaż użytkownikowi ścieżkę, nie wklejaj całości.
- Jeśli plik pomysłu nie istnieje, zapytaj użytkownika o opis pomysłu i zapisz go
  do tymczasowego `idea.md` przed uruchomieniem.

> UWAGA: ta kopia jest wersjonowana w repo. Kopia instalacyjna (używana przez
> agenta) znajduje się w `~/.claude/skills/boardroom/SKILL.md` — po zmianach
> tutaj skopiuj ją tam.
