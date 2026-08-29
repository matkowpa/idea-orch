#!/usr/bin/env python3
"""Raport kosztów sesji Boardroom na podstawie run.log.

Użycie:
    python cost_report.py <katalog-sesji-lub-slug> [--no-fetch]

Czyta sessions/<slug>/run.log, sumuje tokeny per model i liczy koszt.
Ceny pobierane z API OpenRouter (cache: pricing_cache.json); przy braku
połączenia — fallback na cennik z plan-idea-orch.md §7 (2026-08-29).
"""

import argparse
import json
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CACHE_FILE = BASE_DIR / "pricing_cache.json"

# ceny per 1M tokenów (input, output) — fallback wg plan-idea-orch.md §7
FALLBACK_PRICES = {
    "openrouter/anthropic/claude-sonnet-5": (2.00, 10.00),
    "openrouter/z-ai/glm-5.3": (1.20, 4.00),
    "openrouter/openai/gpt-5.1": (1.25, 10.00),
    "openrouter/openai/gpt-5-mini": (0.25, 2.00),
}

OPENROUTER_MODELS_URL = "https://openrouter.ai/api/v1/models"


def parse_run_log(path: Path) -> list[dict]:
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("status") == "ok":
            entries.append(e)
    return entries


def _load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def _save_cache(cache: dict) -> None:
    CACHE_FILE.write_text(json.dumps(cache, indent=1), encoding="utf-8")


def _fetch_prices_from_api(models: list[str]) -> dict[str, tuple[float, float]]:
    """Ceny (per 1M tokenów) z API OpenRouter dla podanych pełnych slug-ów."""
    needed = {m.split("/", 1)[1] for m in models if "/" in m}
    out: dict[str, tuple[float, float]] = {}
    with urllib.request.urlopen(OPENROUTER_MODELS_URL, timeout=15) as resp:
        data = json.load(resp)
    for m in data.get("data", []):
        if m.get("id") in needed:
            p = m.get("pricing", {})
            try:
                in_per_tok = float(p.get("prompt", 0) or 0)
                out_per_tok = float(p.get("completion", 0) or 0)
            except (TypeError, ValueError):
                continue
            out["openrouter/" + m["id"]] = (in_per_tok * 1e6, out_per_tok * 1e6)
    return out


def get_prices(models: list[str], fetch: bool = True) -> dict[str, tuple[float, float]]:
    """Ceny per model: cache -> API OpenRouter -> FALLBACK_PRICES."""
    missing = [m for m in models if m not in FALLBACK_PRICES]
    prices = dict(FALLBACK_PRICES)
    if missing and fetch:
        cache = _load_cache()
        for m in missing:
            if m in cache:
                prices[m] = tuple(cache[m])
        still_missing = [m for m in missing if m not in prices]
        if still_missing:
            try:
                fetched = _fetch_prices_from_api(still_missing)
                for m, p in fetched.items():
                    prices[m] = p
                    cache[m] = list(p)
                _save_cache(cache)
            except Exception as exc:  # noqa: BLE001 — offline/fallback
                print(f"  (ceny z API niedostępne: {exc}; używam fallbacku)", file=sys.stderr)
    return prices


def build_report(session_dir: Path, fetch: bool = True) -> tuple[str, float]:
    log_path = session_dir / "run.log"
    if not log_path.exists():
        raise FileNotFoundError(f"Brak run.log w {session_dir}")
    entries = parse_run_log(log_path)
    if not entries:
        return ("## Raport kosztów\n\nBrak udanych wywołań w `run.log`.\n", 0.0)

    models = sorted({e["model"] for e in entries})
    prices = get_prices(models, fetch=fetch)

    agg: dict[str, dict] = {}
    for e in entries:
        a = agg.setdefault(e["model"], {"calls": 0, "in": 0, "out": 0, "cost": 0.0})
        a["calls"] += 1
        pt = e.get("prompt_tokens") or 0
        ct = e.get("completion_tokens") or 0
        a["in"] += pt
        a["out"] += ct
        pin, pout = prices.get(e["model"], (0.0, 0.0))
        a["cost"] += pt / 1e6 * pin + ct / 1e6 * pout

    total = sum(a["cost"] for a in agg.values())
    lines = [
        "# Raport kosztów sesji",
        "",
        f"_{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_",
        "",
        "| Model | Wywołania | Tokeny in | Tokeny out | Koszt (USD) |",
        "|---|---|---|---|---|",
    ]
    for m in models:
        a = agg[m]
        lines.append(f"| `{m}` | {a['calls']} | {a['in']:,} | {a['out']:,} | ${a['cost']:.4f} |")
    lines += ["", f"**RAZEM: ${total:.4f}**", ""]
    return "\n".join(lines), total


def report(session_dir: Path, fetch: bool = True) -> float:
    """Wygeneruj cost_report.md w sesji, wydrukuj podsumowanie, zwróć koszt."""
    text, total = build_report(session_dir, fetch=fetch)
    out = session_dir / "cost_report.md"
    out.write_text(text, encoding="utf-8")
    print(f"\nKoszt sesji: ${total:.4f} (raport: {out})")
    return total


def main() -> None:
    parser = argparse.ArgumentParser(description="Raport kosztów sesji Boardroom")
    parser.add_argument("session", help="katalog sesji albo slug (sessions/<slug>)")
    parser.add_argument("--no-fetch", action="store_true",
                        help="nie pobieraj cen z API (tylko cache/fallback)")
    args = parser.parse_args()

    p = Path(args.session)
    if not p.exists():
        p = BASE_DIR / "sessions" / args.session
    try:
        report(p, fetch=not args.no_fetch)
    except FileNotFoundError as exc:
        sys.exit(str(exc))


if __name__ == "__main__":
    main()
