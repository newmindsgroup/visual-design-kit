#!/usr/bin/env python3
"""Summarize `claude plugin eval --json` output for the Visual Design Kit eval loop.

Usage:
  python3 summarize_eval.py RESULT.json                 # per-case table (markdown)
  python3 summarize_eval.py RESULT.json --failures      # also list failing graders per run
  python3 summarize_eval.py BEFORE.json AFTER.json      # compare two runs case by case

RESULT.json is the file written by `--json <path>` or an `evals/results/<ts>/aggregate-result.json`.
Standard library only; Python 3.9+.
"""
import argparse
import json
import sys


def load(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def fmt(value):
    if value is None:
        return "n/a"
    return "{:.2f}".format(value)


def indicator(case):
    """Share of with-arm runs in which every with-only indicator (skill fired) passed."""
    names = {
        g.get("name")
        for g in case.get("graders", [])
        if g.get("type") == "tool_used" and (g.get("config") or {}).get("arm") == "with-only"
    }
    runs = case.get("arms", {}).get("with", [])
    flags = []
    for run in runs:
        marks = [g.get("passed") for g in run.get("graders", []) if g.get("withOnly") or g.get("name") in names]
        if marks:
            flags.append(all(marks))
    if not flags:
        return "-"
    return "{}/{}".format(sum(1 for f in flags if f), len(flags))


def arm_cost(case):
    total = 0.0
    for runs in case.get("arms", {}).values():
        for run in runs:
            total += (run.get("costUsd") or 0) + (run.get("judgeCostUsd") or 0)
    return total


def verdict(agg):
    with_score = agg.get("score")
    without = agg.get("scoreWithout")
    if without is None:
        return "with-only run"
    delta = agg.get("delta", (with_score or 0) - (without or 0))
    if delta < 0:
        return "REGRESSION"
    if with_score is not None and with_score >= 0.67 and without >= 0.67:
        return "no lift (harden or keep as guard)"
    if with_score is not None and with_score < 0.67:
        return "triage (kit or grader)"
    return "lift"


def table(result, show_failures=False):
    lines = [
        "| Case | With | Without | Delta | Skill fired | Cost USD | Reading |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    failures = []
    for case in result.get("cases", []):
        agg = case.get("aggregates", {})
        lines.append(
            "| `{}` | {} | {} | {} | {} | {:.2f} | {} |".format(
                case.get("name"),
                fmt(agg.get("score")),
                fmt(agg.get("scoreWithout")),
                fmt(agg.get("delta")),
                indicator(case),
                arm_cost(case),
                verdict(agg),
            )
        )
        if show_failures:
            for arm, runs in case.get("arms", {}).items():
                for index, run in enumerate(runs, 1):
                    if run.get("error"):
                        failures.append("{} [{} run {}] ERROR {}".format(case.get("name"), arm, index, run["error"]))
                    for grader in run.get("graders", []):
                        if not grader.get("passed"):
                            failures.append(
                                "{} [{} run {}] {}: {}".format(
                                    case.get("name"), arm, index, grader.get("name"),
                                    (grader.get("explanation") or "").replace("\n", " ")[:300],
                                )
                            )
    overall = result.get("aggregates", {})
    lines.append("")
    lines.append(
        "Claude {} | ablation {} | cost ${:.2f} | partial {} | overall score {}".format(
            result.get("claudeVersion"),
            result.get("suite", {}).get("ablation"),
            result.get("costUsd") or 0,
            result.get("partial"),
            fmt(overall.get("overallScore")),
        )
    )
    if failures:
        lines.append("")
        lines.append("Failing graders:")
        lines.extend("- " + item for item in failures)
    return "\n".join(lines)


def compare(before, after):
    old = {c["name"]: c.get("aggregates", {}) for c in before.get("cases", [])}
    lines = [
        "| Case | With before | With after | Delta before | Delta after | Change |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for case in after.get("cases", []):
        name = case["name"]
        new = case.get("aggregates", {})
        prev = old.get(name, {})
        change = "new case"
        if prev:
            diff = (new.get("score") or 0) - (prev.get("score") or 0)
            change = "better" if diff > 0 else ("WORSE" if diff < 0 else "same")
        lines.append(
            "| `{}` | {} | {} | {} | {} | {} |".format(
                name, fmt(prev.get("score")), fmt(new.get("score")),
                fmt(prev.get("delta")), fmt(new.get("delta")), change,
            )
        )
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("results", nargs="+", help="one result JSON, or BEFORE and AFTER")
    parser.add_argument("--failures", action="store_true", help="list failing graders per run")
    args = parser.parse_args(argv)
    if len(args.results) == 1:
        print(table(load(args.results[0]), args.failures))
    elif len(args.results) == 2:
        print(compare(load(args.results[0]), load(args.results[1])))
    else:
        parser.error("pass one result file, or two to compare")
    return 0


if __name__ == "__main__":
    sys.exit(main())
