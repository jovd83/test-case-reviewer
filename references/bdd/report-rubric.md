# Report Rubric

Use this file when the user asks for a formal report, score, executive summary, or coaching-oriented assessment.

## When to use the formal report

Use it for:

- structured review reports
- executive or lead-level summaries
- quality scores
- coaching-heavy feedback
- traceability and coverage assessments
- publish-or-reject style artifact reviews

## Required report inputs

Capture:

- artifact scope
- oracle sources used
- oracle sufficiency
- review confidence
- requested decision or deliverable

## Findings format

For each finding, include:

1. severity
2. affected artifact
3. evidence
4. issue
5. why it matters
6. recommended fix

## Severity guide

- `Critical`: the behavior is wrong, contradictory, missing, or too ambiguous to trust
- `High`: the artifact is likely to mislead implementation, review, automation, or sign-off
- `Medium`: a real quality defect with limited reach, such as one weak outcome or a readable but mixed scenario
- `Low`: wording, readability, metadata, or low-risk cleanup

## Scoring guide

Use a 10-point scale only when the user asks for a score.

- `9-10`: strong artifact, reusable with only minor cleanup
- `7-8`: solid artifact, but moderate improvements would materially help
- `5-6`: usable draft, but notable rework is still needed
- `3-4`: below standard and likely to mislead the team
- `1-2`: major rework required before the artifact should be trusted

Do not force a score when the user did not ask for one.

## Report structure

Use this order:

1. executive summary
2. oracle and confidence statement
3. findings by severity
4. traceability and coverage assessment
5. BDD quality assessment
6. standards compliance assessment
7. coaching recommendations
8. action plan

## Reporting rules

- Put findings before praise.
- Keep praise short and specific.
- Distinguish confirmed defects from missing information.
- Mark blocked decisions explicitly.
- Include corrected example wording when it materially speeds up learning.
