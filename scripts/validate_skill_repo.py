from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "agents/openai.yaml",
    "assets/bdd-feature-template.feature",
    "assets/bdd-review-report-template.md",
    "references/bdd/quality-rules.md",
    "references/bdd/feature-and-scenario-protocol.md",
    "references/bdd/intake-and-decision-flow.md",
    "references/bdd/output-contracts.md",
    "references/bdd/report-rubric.md",
    "references/bdd/review-workflow.md",
    "references/test-cases/review-workflow.md",
    "references/test-cases/test-case-protocol.md",
    "references/test-cases/test-suite-protocol.md",
    "references/test-cases/report-template.md",
    "references/test-cases/examples-test-case-quality.md",
    "references/test-cases/examples-review-comments.md",
    "references/test-cases/examples-mini-review-reports.md",
    "references/test-cases/examples-bad-input-artifacts.md",
    "eval/behavior-checklist.md",
    "eval/forward-evals.json",
    "eval/forward-test-matrix.md",
    "eval/trigger-evals.json",
    "examples/bdd/formal-report-request.md",
    "examples/bdd/generation-source.md",
    "examples/bdd/review-input.feature",
    "examples/bdd/review-oracle.md",
    "examples/bdd/review-request.md",
    "examples/bdd/rewrite-request.md",
    "examples/bdd/rewrite-source.feature",
    "examples/bdd/hybrid-source.feature",
]

SKILL_ALLOWED_FIELDS = {"name", "description", "license", "metadata", "allowed-tools"}
SKILL_REQUIRED_FIELDS = {"name", "description"}
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str) -> None:
    print(f"FAIL: {message}")


def ok(message: str) -> None:
    print(f"PASS: {message}")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("SKILL.md frontmatter is not properly closed")

    raw = parts[1]
    result: dict[str, str] = {}

    for line in raw.splitlines():
        if not line or line.startswith(" ") or line.startswith("\t"):
            continue
        stripped = line.strip()
        if ":" not in stripped:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = stripped.split(":", 1)
        result[key.strip()] = value.strip().strip('"')

    return result


def validate_skill_md(root: Path, errors: list[str]) -> None:
    path = root / "SKILL.md"
    data = parse_frontmatter(path)

    missing = sorted(SKILL_REQUIRED_FIELDS - data.keys())
    if missing:
        errors.append(f"SKILL.md is missing required frontmatter fields: {', '.join(missing)}")

    unknown = sorted(set(data) - SKILL_ALLOWED_FIELDS)
    if unknown:
        errors.append(f"SKILL.md has unsupported frontmatter fields: {', '.join(unknown)}")

    name = data.get("name", "")
    if name and not SKILL_NAME_PATTERN.match(name):
        errors.append("SKILL.md name must use lowercase letters, digits, and hyphens only")
    if len(name) > 64:
        errors.append("SKILL.md name exceeds 64 characters")

    description = data.get("description", "")
    if not description:
        errors.append("SKILL.md description must be non-empty")
    if len(description) > 1024:
        errors.append("SKILL.md description exceeds 1024 characters")


def validate_openai_yaml(root: Path, errors: list[str]) -> None:
    text = (root / "agents" / "openai.yaml").read_text(encoding="utf-8")
    required_snippets = [
        "interface:",
        "display_name:",
        "short_description:",
        "default_prompt:",
        "policy:",
        "allow_implicit_invocation:",
    ]
    for snippet in required_snippets:
        if snippet not in text:
            errors.append(f"agents/openai.yaml is missing `{snippet}`")


def validate_trigger_evals(root: Path, errors: list[str]) -> None:
    path = root / "eval" / "trigger-evals.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"eval/trigger-evals.json is not valid JSON: {exc}")
        return

    if not isinstance(data, list) or not data:
        errors.append("eval/trigger-evals.json must contain a non-empty array")
        return

    seen_queries: set[str] = set()
    has_positive = False
    has_negative = False

    for idx, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            errors.append(f"trigger eval #{idx} is not an object")
            continue
        if not isinstance(item.get("query"), str) or not item["query"].strip():
            errors.append(f"trigger eval #{idx} must have a non-empty string `query`")
        elif item["query"] in seen_queries:
            errors.append(f"trigger eval #{idx} duplicates an earlier query")
        else:
            seen_queries.add(item["query"])
        if not isinstance(item.get("should_trigger"), bool):
            errors.append(f"trigger eval #{idx} must have a boolean `should_trigger`")
        elif item["should_trigger"]:
            has_positive = True
        else:
            has_negative = True

    if not has_positive:
        errors.append("eval/trigger-evals.json must include at least one positive trigger case")
    if not has_negative:
        errors.append("eval/trigger-evals.json must include at least one negative trigger case")


def validate_forward_evals(root: Path, errors: list[str]) -> None:
    path = root / "eval" / "forward-evals.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"eval/forward-evals.json is not valid JSON: {exc}")
        return

    if not isinstance(data, dict):
        errors.append("eval/forward-evals.json must contain a JSON object")
        return

    skill_name = data.get("skill_name")
    if not isinstance(skill_name, str) or not skill_name.strip():
        errors.append("eval/forward-evals.json must include a non-empty string `skill_name`")

    evals = data.get("evals")
    if not isinstance(evals, list) or not evals:
        errors.append("eval/forward-evals.json must contain a non-empty `evals` array")
        return

    seen_ids: set[int] = set()
    for idx, item in enumerate(evals, start=1):
        if not isinstance(item, dict):
            errors.append(f"forward eval #{idx} is not an object")
            continue

        eval_id = item.get("id")
        if not isinstance(eval_id, int):
            errors.append(f"forward eval #{idx} must have an integer `id`")
        elif eval_id in seen_ids:
            errors.append(f"forward eval #{idx} duplicates eval id {eval_id}")
        else:
            seen_ids.add(eval_id)

        if not isinstance(item.get("prompt"), str) or not item["prompt"].strip():
            errors.append(f"forward eval #{idx} must have a non-empty string `prompt`")

        if not isinstance(item.get("expected_output"), str) or not item["expected_output"].strip():
            errors.append(f"forward eval #{idx} must have a non-empty string `expected_output`")

        files = item.get("files")
        if not isinstance(files, list):
            errors.append(f"forward eval #{idx} must have a `files` array")
        else:
            for file_idx, file_path in enumerate(files, start=1):
                if not isinstance(file_path, str) or not file_path.strip():
                    errors.append(
                        f"forward eval #{idx} file entry #{file_idx} must be a non-empty string"
                    )
                    continue
                if not (root / file_path).exists():
                    errors.append(f"forward eval #{idx} references a missing file: {file_path}")

        expectations = item.get("expectations")
        if not isinstance(expectations, list) or not expectations:
            errors.append(f"forward eval #{idx} must have a non-empty `expectations` array")
        else:
            for exp_idx, expectation in enumerate(expectations, start=1):
                if not isinstance(expectation, str) or not expectation.strip():
                    errors.append(
                        f"forward eval #{idx} expectation #{exp_idx} must be a non-empty string"
                    )


def validate_template(root: Path, errors: list[str]) -> None:
    text = (root / "assets" / "bdd-feature-template.feature").read_text(encoding="utf-8")
    forbidden_defaults = [
        "\n@requirement-",
        "\n@persona-",
        "\n@test-level-",
        "\n@manual",
        "\n@automated",
    ]
    for snippet in forbidden_defaults:
        if snippet in text:
            errors.append(
                "assets/bdd-feature-template.feature must not force default metadata tags; comment them out or remove them"
            )
            break


def validate_required_files(root: Path, errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (root / relative).exists():
            errors.append(f"Missing required file: {relative}")


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    errors: list[str] = []

    validate_required_files(root, errors)
    if errors:
        for error in errors:
            fail(error)
        return 1

    try:
        validate_skill_md(root, errors)
    except Exception as exc:
        errors.append(f"Unable to validate SKILL.md frontmatter: {exc}")

    validate_openai_yaml(root, errors)
    validate_trigger_evals(root, errors)
    validate_forward_evals(root, errors)
    validate_template(root, errors)

    if errors:
        for error in errors:
            fail(error)
        return 1

    ok("required files are present")
    ok("SKILL.md frontmatter looks valid")
    ok("agents/openai.yaml includes required interface fields")
    ok("trigger evals are valid JSON with the expected shape")
    ok("forward eval manifest is valid and references existing files")
    ok("feature template does not force invented tags")
    print("Repository validation succeeded.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
