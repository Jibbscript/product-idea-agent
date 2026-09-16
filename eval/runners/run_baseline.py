#!/usr/bin/env python3
"""
Baseline Evaluation Runner

Runs product validation workflow WITHOUT skill pack for baseline comparison.
This establishes the "no skills" benchmark to measure skill pack improvement.

Usage:
    python run_baseline.py [--fixture FIXTURE_ID] [--output OUTPUT_DIR]

Example:
    python run_baseline.py --fixture t1-energy-audit
    python run_baseline.py --all
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# Evaluation configuration
EVAL_DIR = Path(__file__).parent.parent
FIXTURES_DIR = EVAL_DIR / "fixtures"
RESULTS_DIR = EVAL_DIR / "results"

# Baseline prompt template (no skills)
BASELINE_PROMPT = """
You are helping validate a product idea. Please analyze the following idea and produce a comprehensive validation report.

## The Idea

{idea_input}

## Your Task

Please produce the following deliverables:

1. **Idea Brief** (idea_brief.md): Structure the idea with problem statement, target customer, solution hypothesis, and key assumptions.

2. **Demand Signals** (signals.md): Research and document search trends, community discussions, and market interest indicators.

3. **ICP Definition** (icp.yaml): Define the ideal customer profile with demographics, psychographics, and behaviors.

4. **Competitive Landscape** (competitors.csv): Map direct and indirect competitors with analysis.

5. **Market Sizing** (market_size.md): Estimate TAM, SAM, and SOM with methodology.

6. **Pricing Research** (pricing.yaml): Analyze competitor pricing and estimate willingness-to-pay.

7. **MVP Spec** (mvp_spec.md): Define MVP scope, technical approach, and differentiation.

8. **GTM Plan** (gtm_plan.md): Identify go-to-market channels and launch strategy.

9. **Risk Assessment** (risks.md): Identify and score risks with mitigations.

10. **Scorecard** (scorecard.json): Score the opportunity across dimensions and provide recommendation.

11. **Validation Report** (validation_report.md): Synthesize all findings into an executive report.

Cite a source for every number and every named company.
"""


def load_fixture(fixture_id: str) -> dict:
    """Load a test fixture by ID."""
    fixture_dir = FIXTURES_DIR / fixture_id

    if not fixture_dir.exists():
        raise ValueError(f"Fixture not found: {fixture_id}")

    # Load input
    input_path = fixture_dir / "input.md"
    if not input_path.exists():
        raise ValueError(f"No input.md found in fixture: {fixture_id}")

    with open(input_path, "r") as f:
        input_content = f.read()

    # Load rubric
    rubric_path = fixture_dir / "rubric.yaml"
    rubric = None
    if rubric_path.exists():
        import yaml
        with open(rubric_path, "r") as f:
            rubric = yaml.safe_load(f)

    # Load expected outputs
    expected_outputs = {}
    expected_dir = fixture_dir / "expected_outputs"
    if expected_dir.exists():
        for file_path in expected_dir.iterdir():
            with open(file_path, "r") as f:
                expected_outputs[file_path.name] = f.read()

    return {
        "id": fixture_id,
        "input": input_content,
        "rubric": rubric,
        "expected_outputs": expected_outputs
    }


def generate_baseline_prompt(fixture: dict) -> str:
    """Generate the baseline prompt for a fixture."""
    return BASELINE_PROMPT.format(idea_input=fixture["input"])


def run_baseline_evaluation(fixture_id: str, output_dir: Optional[Path] = None) -> dict:
    """
    Run baseline evaluation for a fixture.

    Note: This function generates the prompt but actual LLM execution
    should be done separately (e.g., via Claude API or Claude Code).
    """
    fixture = load_fixture(fixture_id)
    prompt = generate_baseline_prompt(fixture)

    # Create output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = RESULTS_DIR / f"baseline_{fixture_id}_{timestamp}"

    output_dir.mkdir(parents=True, exist_ok=True)

    # Save the prompt for manual execution
    prompt_path = output_dir / "baseline_prompt.md"
    with open(prompt_path, "w") as f:
        f.write(prompt)

    # Save fixture info
    info = {
        "fixture_id": fixture_id,
        "mode": "baseline",
        "timestamp": datetime.now().isoformat(),
        "prompt_file": str(prompt_path),
        "expected_outputs": list(fixture["expected_outputs"].keys()),
        "status": "prompt_generated"
    }

    info_path = output_dir / "evaluation_info.json"
    with open(info_path, "w") as f:
        json.dump(info, f, indent=2)

    print(f"Baseline evaluation prepared for: {fixture_id}")
    print(f"Output directory: {output_dir}")
    print(f"Prompt saved to: {prompt_path}")
    print()
    print("Next steps:")
    print("1. Run the prompt through Claude (API or Claude Code)")
    print("2. Save the generated artifacts to the output directory")
    print("3. Run scoring with: python score_results.py --dir {output_dir}")

    return info


def list_fixtures() -> list[str]:
    """List all available fixtures."""
    fixtures = []
    for item in FIXTURES_DIR.iterdir():
        if item.is_dir() and (item / "input.md").exists():
            fixtures.append(item.name)
    return sorted(fixtures)


def main():
    parser = argparse.ArgumentParser(description="Run baseline product validation evaluation")
    parser.add_argument(
        "--fixture", "-f",
        type=str,
        help="Fixture ID to evaluate (e.g., t1-energy-audit)"
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Run all fixtures"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List available fixtures"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        help="Output directory for results"
    )

    args = parser.parse_args()

    if args.list:
        print("Available fixtures:")
        for fixture in list_fixtures():
            print(f"  - {fixture}")
        return

    if args.all:
        fixtures = list_fixtures()
    elif args.fixture:
        fixtures = [args.fixture]
    else:
        parser.print_help()
        return

    for fixture_id in fixtures:
        try:
            output_dir = Path(args.output) if args.output else None
            run_baseline_evaluation(fixture_id, output_dir)
            print()
        except Exception as e:
            print(f"Error evaluating {fixture_id}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
