#!/usr/bin/env python3
"""Integrity checks of eval/fable_prompt_bench.py, observed through its CLI output.

Each test copies the pack's prompt surface to a temp dir, breaks one thing,
runs the benchmark there, and reads the `!!` integrity lines it prints.

Usage:  python3 -m unittest eval/test_fable_prompt_bench.py
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = [".claude-plugin", "skills", "contracts", "eval/runners", "eval/fable_prompt_bench.py"]


def integrity_lines(mutate=lambda root: None) -> list[str]:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for rel in COPY:
            src, dst = ROOT / rel, root / rel
            if src.is_dir():
                shutil.copytree(src, dst)
            elif src.exists():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        mutate(root)
        out = subprocess.run([sys.executable, str(root / "eval/fable_prompt_bench.py")],
                             capture_output=True, text=True, check=True).stdout
    return [l for l in out.splitlines() if "!!" in l]


def rewrite(root: Path, skill: str, old: str, new: str) -> None:
    path = root / "skills" / skill / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{old!r} not in {skill}"
    path.write_text(text.replace(old, new), encoding="utf-8")


class ContractReferences(unittest.TestCase):
    def test_bare_contract_path_is_an_integrity_failure(self):
        lines = integrity_lines(lambda r: rewrite(
            r, "demand-signals", "${CLAUDE_PLUGIN_ROOT}/contracts/signals.md", "contracts/signals.md"))
        self.assertTrue(any(l.startswith("demand-signals") and "CLAUDE_PLUGIN_ROOT" in l for l in lines), lines)

    def test_missing_contract_file_is_an_integrity_failure(self):
        lines = integrity_lines(lambda r: rewrite(
            r, "market-sizing", "contracts/market_size.md", "contracts/market_sizes.md"))
        self.assertTrue(any(l.startswith("market-sizing") and "market_sizes.md" in l for l in lines), lines)


class PackName(unittest.TestCase):
    def test_pack_that_differs_from_plugin_name_is_an_integrity_failure(self):
        def rename_plugin(root: Path) -> None:
            manifest = root / ".claude-plugin/plugin.json"
            manifest.write_text(manifest.read_text().replace('"name": "product-idea-agent"', '"name": "idea-lab"', 1))
        lines = integrity_lines(rename_plugin)
        self.assertEqual(12, sum("idea-lab" in l for l in lines), lines)


class CleanPack(unittest.TestCase):
    def test_repository_has_no_integrity_failures(self):
        self.assertEqual([], integrity_lines())


if __name__ == "__main__":
    unittest.main()
