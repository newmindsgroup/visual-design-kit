"""Weighted scoring and sensitivity check for design directions.

Version-Timestamp: 2026-10-20 02:05:00 UTC

Usage:
  python3 score_directions.py scores.json            # markdown table + sensitivity
  python3 score_directions.py scores.json --json     # machine-readable

scores.json:
{
  "preset": "regulated",                 # or omit and give "weights": {criterion: weight, ...}
  "directions": {
    "A Clean Bright": {"objective": 3, "audience": 4, ...},
    "B Casa": {...}
  },
  "notes": {"A Clean Bright": {"objective": "one-line evidence", ...}}   # optional
}

Standard library only. Scores are 1-5; weights are renormalized to sum to 100.
"""
import argparse
import json
import sys

CRITERIA = ["objective", "audience", "differentiation", "brand", "accessibility", "feasibility", "scalability", "longevity", "risk"]
LABELS = {"objective": "Objective fit", "audience": "Audience fit", "differentiation": "Differentiation", "brand": "Brand truth",
          "accessibility": "Accessibility and inclusion", "feasibility": "Feasibility", "scalability": "Scalability",
          "longevity": "Longevity", "risk": "Risk"}
PRESETS = {
    "default": [20, 15, 15, 10, 10, 10, 10, 5, 5],
    "launch": [20, 15, 25, 10, 5, 10, 5, 5, 5],
    "regulated": [15, 15, 10, 10, 20, 10, 5, 5, 10],
    "rebrand": [15, 15, 15, 20, 10, 5, 10, 10, 0],
    "product-ui": [15, 20, 5, 5, 20, 15, 15, 5, 0],
}


class ScoreError(ValueError):
    pass


def weights_from(spec):
    if "weights" in spec:
        raw = spec["weights"]
        unknown = set(raw) - set(CRITERIA)
        if unknown:
            raise ScoreError(f"unknown criteria in weights: {sorted(unknown)}")
        weights = {c: float(raw.get(c, 0)) for c in CRITERIA}
    else:
        preset = spec.get("preset", "default")
        if preset not in PRESETS:
            raise ScoreError(f"unknown preset {preset}; choose from {sorted(PRESETS)}")
        weights = dict(zip(CRITERIA, map(float, PRESETS[preset])))
    total = sum(weights.values())
    if total <= 0 or any(w < 0 for w in weights.values()):
        raise ScoreError("weights must be non-negative and not all zero")
    return {c: w * 100 / total for c, w in weights.items()}


def validate_scores(directions):
    if len(directions) < 2:
        raise ScoreError("score at least two directions")
    for name, scores in directions.items():
        missing = [c for c in CRITERIA if c not in scores]
        if missing:
            raise ScoreError(f"{name} is missing scores for {missing}")
        for c in CRITERIA:
            value = scores[c]
            if not isinstance(value, (int, float)) or not 1 <= value <= 5:
                raise ScoreError(f"{name}.{c} must be a number from 1 to 5")


def weighted(directions, weights):
    return {name: sum(scores[c] * weights[c] for c in CRITERIA) / 100 for name, scores in directions.items()}


def winner(results):
    ordered = sorted(results.items(), key=lambda pair: (-round(pair[1], 6), pair[0]))
    return ordered[0][0], ordered


def sensitivity(directions, weights, step=10):
    base_winner, _ = winner(weighted(directions, weights))
    flips = []
    for criterion in CRITERIA:
        for delta in (step, -step):
            target = max(0.0, min(100.0, weights[criterion] + delta))
            if abs(target - weights[criterion]) < 1e-9:
                continue
            others = sum(w for c, w in weights.items() if c != criterion)
            if others <= 0:
                continue
            scale = (100 - target) / others
            shifted = {c: (target if c == criterion else w * scale) for c, w in weights.items()}
            results = weighted(directions, shifted)
            top, ordered = winner(results)
            tie = len(ordered) > 1 and abs(ordered[0][1] - ordered[1][1]) < 0.005
            if top != base_winner or tie:
                flips.append({"criterion": criterion, "delta": delta, "results": {k: round(v, 2) for k, v in results.items()},
                              "winner": "tie" if tie else top})
    return base_winner, flips


def report(spec):
    directions = spec["directions"]
    validate_scores(directions)
    weights = weights_from(spec)
    results = weighted(directions, weights)
    top, ordered = winner(results)
    base, flips = sensitivity(directions, weights)
    return {"weights": {c: round(w, 1) for c, w in weights.items()}, "scores": {k: round(v, 2) for k, v in results.items()},
            "ranking": [name for name, _ in ordered], "winner": top,
            "margin": round(ordered[0][1] - ordered[1][1], 2), "sensitivity": flips}


def markdown(spec, result):
    names = list(spec["directions"])
    notes = spec.get("notes", {})
    lines = ["| Criterion (weight) | " + " | ".join(names) + " |", "| --- |" + " --- |" * len(names)]
    for c in CRITERIA:
        cells = []
        for name in names:
            note = notes.get(name, {}).get(c)
            cells.append(f"{spec['directions'][name][c]}" + (f": {note}" if note else ""))
        lines.append(f"| {LABELS[c]} ({result['weights'][c]:g}) | " + " | ".join(cells) + " |")
    lines.append("| **Weighted** | " + " | ".join(
        (f"**{result['scores'][n]:.2f}**" if n == result["winner"] else f"{result['scores'][n]:.2f}") for n in names) + " |")
    lines.append("")
    lines.append(f"Winner: **{result['winner']}** by {result['margin']:.2f}.")
    if result["margin"] < 0.2:
        lines.append("Margin under 0.2: present the top two as a deliberate choice and name the deciding question.")
    if result["sensitivity"]:
        lines.append("Sensitivity (weight shifted by 10 points, others renormalized):")
        for flip in result["sensitivity"]:
            direction = "raised" if flip["delta"] > 0 else "lowered"
            lines.append(f"- {LABELS[flip['criterion']]} {direction}: winner becomes {flip['winner']} {flip['results']}")
    else:
        lines.append("Sensitivity: the winner holds under every 10-point weight shift.")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Score design directions with a weighted matrix")
    parser.add_argument("file", help="scores JSON file, or - for stdin")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        spec = json.load(sys.stdin if args.file == "-" else open(args.file, encoding="utf-8"))
        result = report(spec)
    except (OSError, json.JSONDecodeError, ScoreError, KeyError, TypeError) as exc:
        print(f"score error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2) if args.json else markdown(spec, result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
