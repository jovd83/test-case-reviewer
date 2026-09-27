# Intake and Decision Flow

Use this file when the request is ambiguous, mixed, or under-specified.

## 1. Identify the deliverable

Choose the primary deliverable:

- critique only -> `review`
- improved artifact only -> `rewrite`
- new artifact from requirements -> `generate`
- critique plus improved artifact -> `hybrid`
- formal scorecard or executive summary -> `review` plus the formal report contract

## 2. Grade the oracle

Use this oracle sufficiency model:

- `strong`: explicit business rules, acceptance criteria, or authoritative requirements are present
- `partial`: some requirements exist, but important branches or business terms are still missing
- `weak`: only raw scenario text, feature text, or vague notes are present

## 3. Set confidence

Use this confidence model:

- `high`: strong oracle and low ambiguity
- `medium`: partial oracle or limited ambiguity
- `low`: weak oracle, conflicting inputs, or material ambiguity

Do not report `high` confidence when the source of truth is weak.

## 4. Decide whether to proceed or stop

Proceed without blocking questions when:

- the user asked for structural review
- the task is mainly about BDD quality
- a usable rewrite can be produced with explicit assumptions
- a partial generation can still be valuable

Pause and ask only when:

- the wrong assumption would materially change the behavior
- the user expects correctness claims that cannot be justified
- multiple incompatible interpretations are equally plausible

## 5. Choose the output depth

Use a quick pass for:

- one scenario
- one short feature
- lightweight coaching

Use a formal pass for:

- severity-ranked reports
- scorecards
- traceability analysis
- executive summaries
- publish-or-reject review decisions

## 6. Default handling for weak inputs

If the oracle is weak:

- review structure and quality normally
- lower confidence explicitly
- avoid claiming behavioral completeness
- list the blocked decisions or missing rules

## 7. Recommended phrasing

Use phrases like:

- `Oracle sufficiency: partial`
- `Confidence: low because the acceptance criteria do not define the rejection path`
- `The artifact can be improved structurally, but behavioral correctness cannot be confirmed from the provided source`
