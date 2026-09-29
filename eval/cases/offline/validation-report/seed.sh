#!/usr/bin/env bash
# Seeds the run workspace from the t1-energy-audit fixture, the single source for these files.
set -euo pipefail
src="$(dirname "$0")/../../../fixtures/t1-energy-audit"
cp "$src"/expected_outputs/{idea_brief.md,signals.md,icp.yaml,competitors.csv,market_size.md,pricing.yaml,mvp_spec.md,gtm_plan.md,risks.md,scorecard.json} .
