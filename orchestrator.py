#!/usr/bin/env python3
"""Boardroom — orchestrator dyskusji koncepcji biznesowej aplikacji.

Użycie:
    python orchestrator.py --idea path/to/idea.md --name moj-pomysl
"""

import argparse
import asyncio
import datetime
import json
import re
import sys
import time
from pathlib import Path

import litellm
import yaml

BASE_DIR = Path(__file__).resolve().parent

STATUS_RE = re.compile(r"STATUS:\s*(CONTINUE|CONVERGED)", re.IGNORECASE)


# ----------------------------------------------------------------- utilities

def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def render(template: str, **subs) -> str:
    out = template
    for key, val in subs.items():
        out = out.replace("{{" + key + "}}", val)
    return out


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# ------------------------------------------------------------------ LLM call

async def call_model(model: str, system: str, user: str, log, agent: str,
                     temperature: float, max_tokens: int,
                     retries: int = 3) -> str:
    """Jedno wywołanie modelu z retry + logowaniem."""
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]
    last_err = None
    for attempt in range(1, retries + 1):
        start = time.time()
        try:
            resp = await litellm.acompletion(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            text = resp.choices[0].message.content or ""
            usage = getattr(resp, "usage", None)
            log.write(json.dumps({
                "ts": datetime.datetime.now().isoformat(timespec="seconds"),
                "agent": agent, "model": model, "attempt": attempt,
                "duration_s": round(time.time() - start, 1),
                "prompt_tokens": getattr(usage, "prompt_tokens", None),
                "completion_tokens": getattr(usage, "completion_tokens", None),
                "status": "ok",
            }, ensure_ascii=False) + "\n")
            log.flush()
            return text
        except Exception as exc:  # noqa: BLE001 — logujemy i ponawiamy
            last_err = str(exc)
            log.write(json.dumps({
                "ts": datetime.datetime.now().isoformat(timespec="seconds"),
                "agent": agent, "model": model, "attempt": attempt,
                "duration_s": round(time.time() - start, 1),
                "status": "error", "error": last_err,
            }, ensure_ascii=False) + "\n")
            log.flush()
            await asyncio.sleep(2 ** attempt)
    return f"> [ERROR] Agent `{agent}` (model `{model}`) nie odpowiedział: {last_err}"


# ------------------------------------------------------------------ pipeline

class Boardroom:
    def __init__(self, session_dir: Path, cfg: dict):
        self.dir = session_dir
        self.cfg = cfg
        self.log = open(session_dir / "run.log", "a", encoding="utf-8")
        self.idea = read_text(session_dir / "input" / "idea.md")

    def role_of(self, agent: str) -> str:
        return read_text(BASE_DIR / self.cfg["agents"][agent]["role_file"])

    def model_of(self, agent: str) -> str:
        return self.cfg["models"][self.cfg["agents"][agent]["model"]]

    def prompt(self, name: str) -> str:
        return read_text(BASE_DIR / "prompts" / name)

    async def ask(self, agent: str, user: str) -> str:
        return await call_model(
            model=self.model_of(agent),
            system=self.role_of(agent),
            user=user, log=self.log, agent=agent,
            temperature=self.cfg["session"]["temperature"],
            max_tokens=self.cfg["session"]["max_tokens"],
        )

    # ---- etap 1: agenda
    async def build_agenda(self) -> str:
        user = render(self.prompt("01_agenda.md"), IDEA=self.idea)
        agenda = await self.ask("architect", user)
        write_text(self.dir / "01_agenda.md", agenda)
        print("[1/4] Agenda gotowa -> 01_agenda.md")
        return agenda

    # ---- etap 2: kontekst poprzedniej rundy
    def _context_block(self, round_no: int) -> str:
        if round_no == 1:
            return ""
        prev = round_no - 1
        synth_path = self.dir / f"round{prev}" / "_synthesis.md"
        if not synth_path.exists():
            return ""
        prev_ops = []
        for agent in self.cfg["discussing_agents"]:
            p = self.dir / f"round{prev}" / f"{agent}.md"
            body = read_text(p) if p.exists() else "> [brak — błąd]"
            prev_ops.append(f"### OPINIA: {agent}\n\n{body}")
        joined = "\n\n".join(prev_ops)
        limit = self.cfg["session"]["max_discussion_chars"]
        if len(joined) > limit:
            joined = joined[:limit] + "\n\n> [... obcięto: limit kontekstu]"
        return render(self.prompt("_context_block.md"), PREV_ROUND=str(prev),
                      PREV_SYNTHESIS=read_text(synth_path),
                      PREV_OPINIONS=joined)

    # ---- etap 3: runda opinii (równolegle)
    async def discussion_round(self, round_no: int, agenda: str) -> dict:
        context = self._context_block(round_no)
        and_debate = "" if round_no == 1 else " oraz na sporne kwestie z poprzedniej rundy"
        template = self.prompt("02_round_opinion.md")
        tasks = {}
        for agent in self.cfg["discussing_agents"]:
            user = render(template, ROUND=str(round_no), IDEA=self.idea,
                          AGENDA=agenda, CONTEXT=context, AND_DEBATE=and_debate)
            tasks[agent] = asyncio.create_task(self.ask(agent, user))
        results = {a: await t for a, t in tasks.items()}
        for agent, text in results.items():
            write_text(self.dir / f"round{round_no}" / f"{agent}.md", text)
        print(f"[2/4] Runda {round_no}: opinie agentów zapisane.")
        return results

    # ---- etap 4: moderacja
    async def moderate(self, round_no: int, opinions: dict) -> bool:
        ops = [f"### OPINIA: {a}\n\n{opinions[a]}"
               for a in self.cfg["discussing_agents"]]
        user = render(self.prompt("03_moderate.md"), ROUND=str(round_no),
                      OPINIONS="\n\n".join(ops))
        synthesis = await self.ask("moderator", user)
        write_text(self.dir / f"round{round_no}" / "_synthesis.md", synthesis)
        m = STATUS_RE.search(synthesis)
        converged = bool(m) and m.group(1).upper() == "CONVERGED"
        print(f"[3/4] Synteza rundy {round_no} "
              f"({'CONVERGED' if converged else 'CONTINUE'}).")
        return converged

    # ---- etap 5: werdykt końcowy
    async def final_concept(self, rounds: int) -> Path:
        parts = []
        for r in range(1, rounds + 1):
            parts.append(f"## RUNDA {r}\n")
            for agent in self.cfg["discussing_agents"]:
                p = self.dir / f"round{r}" / f"{agent}.md"
                body = read_text(p) if p.exists() else "> [brak — błąd]"
                parts.append(f"### OPINIA: {agent}\n\n{body}\n")
            synth = self.dir / f"round{r}" / "_synthesis.md"
            if synth.exists():
                parts.append(f"### SYNTEZA MODERATORA\n\n{read_text(synth)}\n")
        user = render(self.prompt("04_concept.md"), IDEA=self.idea,
                      TRANSCRIPT="\n".join(parts))
        concept = await self.ask("judge", user)
        write_text(self.dir / "concept.md", concept)
        print(f"[4/4] Finalna koncepcja -> concept.md")
        return self.dir / "concept.md"

    async def run(self) -> Path:
        agenda = await self.build_agenda()
        rounds_done = 0
        for r in range(1, self.cfg["session"]["rounds"] + 1):
            opinions = await self.discussion_round(r, agenda)
            converged = await self.moderate(r, opinions)
            rounds_done = r
            if converged:
                break
        result = await self.final_concept(rounds_done)
        self.log.close()
        return result


# ---------------------------------------------------------------------- main

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Boardroom — rada modeli nad pomysłem")
    parser.add_argument("--idea", required=True, help="ścieżka do pliku idea.md")
    parser.add_argument("--name", required=True, help="nazwa sesji (slug)")
    parser.add_argument("--config", default=str(BASE_DIR / "config.yaml"))
    args = parser.parse_args()

    cfg = load_yaml(Path(args.config))
    idea_path = Path(args.idea)
    if not idea_path.exists():
        sys.exit(f"Nie znaleziono pliku pomysłu: {idea_path}")

    session_dir = BASE_DIR / "sessions" / args.name
    (session_dir / "input").mkdir(parents=True, exist_ok=True)
    write_text(session_dir / "input" / "idea.md", read_text(idea_path))

    print(f"Boardroom start | sesja: {args.name}")
    result = asyncio.run(Boardroom(session_dir, cfg).run())
    import cost_report
    cost_report.report(session_dir)
    print(f"\nGotowe. Wynik: {result}")


if __name__ == "__main__":
    main()
