"""Smoke-test pipeline'u Boardroom z atrapą litellm.acompletion (bez API).

Uruchomienie:  python test_smoke.py
"""

import asyncio
import shutil
import sys
import tempfile
from pathlib import Path

import orchestrator

BASE = Path(__file__).resolve().parent

CALLS = []
counts = {}


async def fake_acompletion(**kwargs):
    """Zwraca kontrolowane odpowiedzi dla każdej roli agenta."""
    messages = kwargs["messages"]
    system = messages[0]["content"]
    user = messages[1]["content"]
    CALLS.append(system[:20])
    if "ARCHITEKTEM" in system:
        return _resp("## Agenda\n- problem\n## Pytania do rady\n1. Kto kupi?")
    if "SKĘPTYKIEM" in system:
        return _resp("## Zarzuty\n1. Brak rynku\n\n## Co mnie przekonałoby\n- dane")
    if "WISIONEREM" in system:
        return _resp("## Możliwości\n1. Skala\n## Największy potencjał\n- X")
    if "ANALITYKIEM" in system:
        return _resp("## Ocena rynku\n- niszowy\n## Monetyzacja\n- abonament")
    if "MODERATOREM" in system:
        counts["mod"] = counts.get("mod", 0) + 1
        if counts["mod"] == 1:
            return _resp("## Spory\n1. rynek?\nSTATUS: CONTINUE")
        return _resp("## Consensus\n- ok\nSTATUS: CONVERGED")
    if "SĘDZIĄ" in system:
        return _resp("# Koncepcja biznesowa\n## 7. Werdykt: GO")
    return _resp("ok")


def _resp(text):
    class U:
        content = text
    class M:
        message = U()
    class R:
        choices = [M()]
        usage = type("U2", (), {"prompt_tokens": 10, "completion_tokens": 5})()
    return R()


def main():
    # sesja testowa
    tmp = Path(tempfile.mkdtemp(prefix="br-test-"))
    idea = tmp / "idea.md"
    idea.write_text("Aplikacja do dzielenia rachunków w restauracjach.", encoding="utf-8")

    cfg = orchestrator.load_yaml(BASE / "config.yaml")
    cfg["session"]["rounds"] = 2
    session_dir = tmp / "session"
    (session_dir / "input").mkdir(parents=True)
    (session_dir / "input" / "idea.md").write_text(idea.read_text(encoding="utf-8"),
                                                   encoding="utf-8")

    # podmieniamy wywołanie LLM
    orchestrator.litellm.acompletion = fake_acompletion

    board = orchestrator.Boardroom(session_dir, cfg)
    result = asyncio.run(board.run())

    assert result.exists(), "brak concept.md"
    assert (session_dir / "01_agenda.md").exists()
    assert (session_dir / "round1" / "sceptic.md").exists()
    assert (session_dir / "round1" / "_synthesis.md").exists()
    assert (session_dir / "run.log").exists()
    concept = result.read_text(encoding="utf-8")
    assert "Werdykt" in concept
    print("SMOKE-TEST OK ->", result)
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
