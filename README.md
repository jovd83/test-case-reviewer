# Test Case Reviewer

[![Validate Skills](https://github.com/jovd83/test-case-reviewer/actions/workflows/ci.yml/badge.svg)](https://github.com/jovd83/test-case-reviewer/actions/workflows/ci.yml)
[![version](https://img.shields.io/badge/version-2.0.0-blue)](CHANGELOG.md)
[![status](https://img.shields.io/badge/status-stable-3fb950)](SKILL.md)
[![category](https://img.shields.io/badge/category-testing-0a7ea4)](SKILL.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/jovd83)

`test-case-reviewer` reviews, scores and mentors drafted tests before they are executed, automated or signed off: classic test cases and suites as well as BDD/Gherkin feature files. It replaces `agentic-bdd-test-case-mentor` and `tss-test-case-reviewer`.

## What This Skill Does

Drafted tests fail in predictable ways whatever their format: they trace to the wrong source, stop at the happy path, assert "success" instead of something observable, and quietly invent the rules they claim to test. The two predecessor skills caught exactly those failures, one for step-based test cases and one for Gherkin, so they now share one intake and one severity scale, with a track for each format.

The shared intake decides the track (test cases or BDD), the mode, and the oracle. It ranks the sources of truth from approved business rules down to the artifact's own text. It refuses implementation code as the oracle, because tests that mirror the code pass while the business rule is wrong. And it never invents requirement IDs, personas, tags or rules to make an artifact look complete.

- **Test-case track:** inventory, requirement-to-test traceability, suite architecture, MSS/EXT/ERR path coverage, technique fit (equivalence partitions, boundary values, decision tables, state transitions, use case paths), technical correctness of preconditions, steps, expected results and data, standards compliance, and mentoring. The output is a nine-section scored review.
- **BDD track:** four modes. `review` finds anti-patterns and coverage gaps; `rewrite` produces business-readable Gherkin; `generate` drafts scenarios from rules, acceptance criteria or example maps; `hybrid` gives findings plus the corrected feature.

Findings on both tracks are rated `Critical`, `High`, `Medium` or `Low`, each with evidence and the affected requirement or scenario named.

## What This Skill Does Not Do

- **It does not design classic test cases from scratch.** Use `test-design-orchestrator` to derive test cases from requirements, and `test-strategy-skill` for the plan above them.
- **It does not write automation.** No step definitions, Playwright, Cypress or Cucumber code: hand the reviewed artifact to the framework skill.
- **It does not render or export.** Formatting cases for Xray, Zephyr, TestRail or TestLink is `test-management-sync`'s job.
- **It does not judge requirements on their own.** A readiness review of the requirements themselves belongs to `test-analysis-skill`; here they are the oracle.

## When To Use It

Use it when:

- someone asks to review, audit, score or critique drafted test cases, UAT scenarios or a regression set;
- a feature file or set of Gherkin scenarios needs a BDD review, a business-readable rewrite, or scenarios drafted from acceptance criteria;
- a traceability matrix or suite hierarchy needs checking for gaps, redundancy or an overloaded suite;
- a junior tester's work needs mentoring with concrete, prioritised feedback;
- a test-lifecycle chain reaches its case quality gate.

For new test design, automation or requirement analysis, use the sibling skills named above.

## Repository Layout

```
test-case-reviewer/
├── SKILL.md                         # shared intake, severity scale, both tracks
├── agents/openai.yaml               # UI metadata for hosts that read it
├── references/
│   ├── test-cases/                  # review workflow, case and suite protocols,
│   │                                # report template, four graded example sets
│   └── bdd/                         # intake, review workflow, quality rules,
│                                    # feature protocol, rubric, output contracts
├── assets/
│   ├── bdd-feature-template.feature # full feature file skeleton
│   └── bdd-review-report-template.md
├── examples/bdd/                    # review, rewrite, generate and report inputs
├── eval/
│   ├── trigger-evals.json           # 38 trigger and near-miss cases (both tracks)
│   ├── forward-evals.json           # forward tests with expectations (BDD)
│   ├── forward-test-matrix.md
│   └── behavior-checklist.md
├── scripts/validate_skill_repo.py   # packaging validator
└── .github/workflows/               # validate.yml, ci.yml
```

## Installation

```bash
npx skills add jovd83/test-case-reviewer
```

Manual alternative:

```bash
git clone https://github.com/jovd83/test-case-reviewer.git
```

Then place the folder where your agent looks for local skills: `~/.agents/skills/`, `~/.cursor/skills/`, or another IDE-specific directory.

The skill has no dependencies. The validator needs Python 3.11 or later.

## Usage

Ask in plain words; the skill picks the track and mode.

| Request | Track and mode |
|---|---|
| "Review these drafted API test cases against the acceptance criteria" | test cases, review |
| "Mentor this junior tester's UC-14 scenarios and score them" | test cases, review with scoring and mentoring |
| "I have 35 cases in one suite: is the structure OK?" | test cases, suite review |
| "Review this feature file for BDD anti-patterns" | BDD, review |
| "Rewrite these scenarios so they read like business behavior" | BDD, rewrite |
| "Generate Gherkin from these refund rules" | BDD, generate |

## Output Contract

- **Test-case track:** executive summary, requirements and traceability, suite architecture (when relevant), coverage, technical correctness, standards compliance, mentoring plan, scoring matrix, action plan. Template: `references/test-cases/report-template.md`.
- **BDD track:** mode, oracle and confidence, ranked findings, then the artifact for rewrite, generate or hybrid. The formal report uses `references/bdd/report-rubric.md` and `assets/bdd-review-report-template.md`.

## Validation

```bash
python scripts/validate_skill_repo.py .
```

It checks the required files, the SKILL.md frontmatter (name format, a description of 1,024 characters or less), `agents/openai.yaml`, the trigger and forward eval files including the example files they reference, and that the feature template forces no invented tags. `.github/workflows/validate.yml` runs it on every push and pull request.

## Evaluation Strategy

`eval/trigger-evals.json` holds 19 cases that must trigger the skill and 19 that must not, such as writing Playwright tests, drafting new acceptance criteria, or designing test cases from scratch. `eval/forward-evals.json` holds BDD forward tests with explicit expectations, including one where a strong artifact must yield `No material defects identified`. The test-case track is calibrated by the four graded example sets in `references/test-cases/`.

## Contributing

Edit in this repository, then copy the folder to `~/.agents/skills/test-case-reviewer/`. The installed copy is downstream and should never be edited directly.

## License

MIT — see [LICENSE](LICENSE).
