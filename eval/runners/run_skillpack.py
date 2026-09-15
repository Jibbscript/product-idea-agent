#!/usr/bin/env python3
"""
Skill Pack Evaluation Runner

Runs product validation workflow WITH skill pack for evaluation.
Compares results against expected outputs and scores using rubrics.

Usage:
    python run_skillpack.py [--fixture FIXTURE_ID] [--output OUTPUT_DIR]

Example:
    python run_skillpack.py --fixture t1-energy-audit
    python run_skillpack.py --all
    python run_skillpack.py --score --dir results/skillpack_t1-energy-audit_20241226/
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional
import re

# Evaluation configuration
EVAL_DIR = Path(__file__).parent.parent
FIXTURES_DIR = EVAL_DIR / "fixtures"
RESULTS_DIR = EVAL_DIR / "results"
SKILLS_DIR = EVAL_DIR.parent / "skills"

# Skill pack prompt template
SKILLPACK_PROMPT = """
You have access to the Product Idea Agent skill pack for comprehensive product validation.

## The Idea

{idea_input}

## Your Task

Use the `idea-validation-orchestrator` skill to run a complete product validation. This will guide you through all 11 validation steps:

1. Create idea brief
2. Research demand signals
3. Define ICP
4. Map competitive landscape
5. Size the market
6. Research pricing
7. Define MVP
8. Plan GTM
9. Assess risks
10. Generate scorecard
11. Compile validation report

Please execute the full workflow and generate all artifacts.
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


def generate_skillpack_prompt(fixture: dict) -> str:
    """Generate the skill pack prompt for a fixture."""
    return SKILLPACK_PROMPT.format(idea_input=fixture["input"])


def run_skillpack_evaluation(fixture_id: str, output_dir: Optional[Path] = None) -> dict:
    """
    Run skill pack evaluation for a fixture.

    Note: This function generates the prompt but actual LLM execution
    should be done via Claude Code with skills installed.
    """
    fixture = load_fixture(fixture_id)
    prompt = generate_skillpack_prompt(fixture)

    # Create output directory
    if output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = RESULTS_DIR / f"skillpack_{fixture_id}_{timestamp}"

    output_dir.mkdir(parents=True, exist_ok=True)

    # Save the prompt for execution
    prompt_path = output_dir / "skillpack_prompt.md"
    with open(prompt_path, "w") as f:
        f.write(prompt)

    # Save expected outputs for comparison
    expected_dir = output_dir / "expected"
    expected_dir.mkdir(exist_ok=True)
    for name, content in fixture["expected_outputs"].items():
        with open(expected_dir / name, "w") as f:
            f.write(content)

    # Save fixture info
    info = {
        "fixture_id": fixture_id,
        "mode": "skillpack",
        "timestamp": datetime.now().isoformat(),
        "prompt_file": str(prompt_path),
        "expected_outputs": list(fixture["expected_outputs"].keys()),
        "rubric": fixture["rubric"],
        "status": "prompt_generated"
    }

    info_path = output_dir / "evaluation_info.json"
    with open(info_path, "w") as f:
        json.dump(info, f, indent=2)

    print(f"Skill pack evaluation prepared for: {fixture_id}")
    print(f"Output directory: {output_dir}")
    print(f"Prompt saved to: {prompt_path}")
    print()
    print("Next steps:")
    print("1. Ensure skills are installed: cp -r skills/* ~/.claude/skills/")
    print("2. Run the prompt in Claude Code")
    print("3. Save the generated artifacts to: {output_dir}/generated/")
    print("4. Run scoring with: python run_skillpack.py --score --dir {output_dir}")

    return info


def score_results(results_dir: Path) -> dict:
    """
    Score generated results against expected outputs.

    Uses rubric to evaluate:
    - Correctness (factual accuracy)
    - Usefulness (actionable insights)
    - Citation quality (sources)
    - Reproducibility (consistency)
    - Time to answer (efficiency)
    """
    results_dir = Path(results_dir)

    # Load evaluation info
    info_path = results_dir / "evaluation_info.json"
    if not info_path.exists():
        raise ValueError(f"No evaluation_info.json found in {results_dir}")

    with open(info_path, "r") as f:
        info = json.load(f)

    # Check for generated outputs
    generated_dir = results_dir / "generated"
    expected_dir = results_dir / "expected"

    if not generated_dir.exists():
        print(f"No generated/ directory found in {results_dir}")
        print("Please save generated artifacts to: {results_dir}/generated/")
        return {"status": "incomplete"}

    # Compare artifacts
    scores = {
        "artifacts_generated": [],
        "artifacts_missing": [],
        "artifact_scores": {},
        "dimension_scores": {},
        "composite_score": 0
    }

    # Check each expected artifact
    for expected_file in info.get("expected_outputs", []):
        generated_path = generated_dir / expected_file
        expected_path = expected_dir / expected_file

        if generated_path.exists():
            scores["artifacts_generated"].append(expected_file)

            # Load contents
            with open(generated_path, "r") as f:
                generated_content = f.read()
            with open(expected_path, "r") as f:
                expected_content = f.read()

            # Basic scoring (placeholder for more sophisticated comparison)
            artifact_score = score_artifact(generated_content, expected_content, expected_file)
            scores["artifact_scores"][expected_file] = artifact_score
        else:
            scores["artifacts_missing"].append(expected_file)

    # Calculate dimension scores from rubric
    rubric = info.get("rubric", {})
    if rubric:
        dimensions = rubric.get("dimensions", {})
        for dim_name, dim_config in dimensions.items():
            weight = dim_config.get("weight", 0.2)
            criteria = dim_config.get("criteria", [])

            # Placeholder: Score based on artifact completion
            completion_rate = len(scores["artifacts_generated"]) / max(len(info.get("expected_outputs", [])), 1)
            dim_score = completion_rate * 100

            scores["dimension_scores"][dim_name] = {
                "score": dim_score,
                "weight": weight,
                "weighted": dim_score * weight
            }

    # Calculate composite score
    if scores["dimension_scores"]:
        total_weighted = sum(d["weighted"] for d in scores["dimension_scores"].values())
        total_weight = sum(d["weight"] for d in scores["dimension_scores"].values())
        scores["composite_score"] = total_weighted / total_weight if total_weight > 0 else 0

    # Save scores
    scores_path = results_dir / "scores.json"
    with open(scores_path, "w") as f:
        json.dump(scores, f, indent=2)

    # Print summary
    print(f"\n=== Evaluation Scores ===")
    print(f"Fixture: {info['fixture_id']}")
    print(f"Mode: {info['mode']}")
    print()
    print(f"Artifacts Generated: {len(scores['artifacts_generated'])}/{len(info.get('expected_outputs', []))}")
    if scores['artifacts_missing']:
        print(f"Missing: {', '.join(scores['artifacts_missing'])}")
    print()
    print(f"Dimension Scores:")
    for dim_name, dim_data in scores.get("dimension_scores", {}).items():
        print(f"  {dim_name}: {dim_data['score']:.1f}%")
    print()
    print(f"Composite Score: {scores['composite_score']:.1f}/100")
    print(f"Scores saved to: {scores_path}")

    return scores


def score_artifact(generated: str, expected: str, filename: str) -> dict:
    """
    Score a single artifact against expected output.

    Returns basic metrics; can be extended for more sophisticated comparison.
    """
    # Basic metrics
    gen_len = len(generated)
    exp_len = len(expected)

    # Word overlap (simple)
    gen_words = set(re.findall(r'\w+', generated.lower()))
    exp_words = set(re.findall(r'\w+', expected.lower()))
    overlap = len(gen_words & exp_words)
    union = len(gen_words | exp_words)
    jaccard = overlap / union if union > 0 else 0

    # Structural checks based on file type
    if filename.endswith('.json'):
        try:
            gen_json = json.loads(generated)
            exp_json = json.loads(expected)
            valid_json = True
            key_overlap = len(set(gen_json.keys()) & set(exp_json.keys())) / max(len(exp_json.keys()), 1)
        except:
            valid_json = False
            key_overlap = 0
    else:
        valid_json = None
        key_overlap = None

    return {
        "generated_length": gen_len,
        "expected_length": exp_len,
        "length_ratio": gen_len / exp_len if exp_len > 0 else 0,
        "word_jaccard": jaccard,
        "valid_json": valid_json,
        "key_overlap": key_overlap
    }


def list_fixtures() -> list[str]:
    """List all available fixtures."""
    fixtures = []
    for item in FIXTURES_DIR.iterdir():
        if item.is_dir() and (item / "input.md").exists():
            fixtures.append(item.name)
    return sorted(fixtures)


def main():
    parser = argparse.ArgumentParser(description="Run skill pack product validation evaluation")
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
    parser.add_argument(
        "--score", "-s",
        action="store_true",
        help="Score results in directory"
    )
    parser.add_argument(
        "--dir", "-d",
        type=str,
        help="Results directory to score"
    )

    args = parser.parse_args()

    if args.list:
        print("Available fixtures:")
        for fixture in list_fixtures():
            print(f"  - {fixture}")
        return

    if args.score:
        if not args.dir:
            print("Error: --dir required when using --score")
            return
        score_results(Path(args.dir))
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
            run_skillpack_evaluation(fixture_id, output_dir)
            print()
        except Exception as e:
            print(f"Error evaluating {fixture_id}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
