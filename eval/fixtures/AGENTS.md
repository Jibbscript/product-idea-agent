<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-09-15 | Updated: 2026-09-15 -->

# fixtures

## Purpose
Five test ideas chosen to span the verdict range. Each fixture directory has the same three parts: `input.md` (the idea plus context, fed into the prompt template), `rubric.yaml` (weighted scoring dimensions plus expected score range and verdict), and `expected_outputs/` (reference artifacts to compare against).

## Subdirectories

| Directory | Idea | Expected composite | Expected verdict | Expected outputs |
|-----------|------|-------------------|------------------|------------------|
| `t1-energy-audit/` | Phone thermal camera for DIY home energy audits, freemium + contractor referrals | 70–85 | GO | all 11 artifacts |
| `t2-fintech-compliance/` | Automated SOC 2 for seed-stage fintech (vs Vanta / Drata / Secureframe) | 55–70 | PIVOT | `scorecard.json` only |
| `t3-synth-collectors/` | Curated marketplace + community for vintage synth collectors | 50–65 | PIVOT | `scorecard.json` only |
| `t4-data-pipeline/` | No-code monitoring for data pipelines (Airflow, dbt, Fivetran) | 60–75 | GO or PIVOT | `scorecard.json` only |
| `t5-plant-subscription/` | Houseplant subscription box with AI care recommendations | 55–70 | PIVOT | `scorecard.json` only |

These directories have no AGENTS.md of their own; this file covers them.

## Key Files (per fixture)

| File | Description |
|------|-------------|
| `input.md` | Title, one-paragraph pitch, `## Additional Context` bullets (target, revenue model, known competitors) |
| `rubric.yaml` | `dimensions:` (correctness, usefulness, citation_quality, reproducibility, time_to_answer) with weighted 1–5 criteria, then `expectations:` with `composite_score_range`, `recommendation`, `key_signals`, `key_risks` |
| `expected_outputs/*` | Reference artifacts named exactly as the pipeline emits them |

## For AI Agents

### Working In This Directory
- Adding a fixture: create `t<N>-<slug>/input.md` (that file alone makes it discoverable), a `rubric.yaml`, and at minimum `expected_outputs/scorecard.json`. Copy the rubric from `t1-energy-audit/` and change only the `expectations:` block.
- Expected outputs must conform to `contracts/`. `t1-energy-audit/expected_outputs/` is the de facto worked example of every contract; when a contract changes, update it.
- The `expectations` block is documentation for a human reviewer. The current scorer ignores it.
- `.DS_Store` files are macOS noise.

### Testing Requirements
- `python eval/runners/run_skillpack.py --list` must show the new fixture.
- `python -c "import yaml; yaml.safe_load(open('eval/fixtures/<id>/rubric.yaml'))"` must succeed.

### Common Patterns
- Fixture ids sort by number prefix; keep `t<N>-` sequential.
- Inputs deliberately name competitors and a revenue model so research skills have anchors to verify against.

## Dependencies

### Internal
- Read by `../runners/run_baseline.py` and `../runners/run_skillpack.py`
- Shapes mirror `../../contracts/`

### External
- None

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
