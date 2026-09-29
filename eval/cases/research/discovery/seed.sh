#!/usr/bin/env bash
# Seeds the run workspace from the t1-energy-audit fixture, the single source for these files.
set -euo pipefail
src="$(dirname "$0")/../../../fixtures/t1-energy-audit"
cp "$src/input.md" .
