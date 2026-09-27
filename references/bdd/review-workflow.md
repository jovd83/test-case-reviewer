# Review Workflow

Use this file for formal, high-confidence, or findings-first BDD reviews.

## 1. Triage the artifact set

Identify:

- artifact type: scenario, feature file, mixed draft, or requirements-only
- requested deliverable: findings list, rewrite, formal report, or generated artifact
- oracle quality: strong, partial, or weak
- expected confidence: high, medium, or low

## 2. Review intent and traceability

Check:

- feature or scenario intent
- business value clarity
- actor or persona clarity when relevant
- links to stories, rules, or requirement IDs when those were provided
- scope boundaries

Flag:

- titles that describe test actions instead of capabilities
- missing or weak business narrative when a feature file is being generated or reviewed as a full feature
- scope ambiguity that blocks reliable review
- missing traceability when the user expected traceability analysis

## 3. Review scenario architecture

Check:

- one scenario per behavior path
- one main event in `When`
- meaningful titles
- duplication or overlap
- grouping by rule, persona, or lifecycle phase when it improves readability

Flag:

- overloaded scenarios
- mixed concerns that belong in separate scenarios or features
- scenario titles like `Test 1`, `Happy path`, or `Check OK`
- features that are too large to remain readable

## 4. Review path coverage

Check:

- main path coverage
- alternate path coverage
- error or rejection coverage
- boundaries, permissions, and lifecycle states when the source makes them relevant

Return:

- covered paths
- missing paths
- business risk created by missing paths

## 5. Review BDD quality

Check:

- business-readable vocabulary
- concrete example quality
- observable outcomes
- minimal but sufficient context
- absence of UI scripting
- absence of implementation leakage

## 6. Review explicit standards only

Check standards compliance only against:

- provided requirements
- explicit team conventions
- explicit metadata schemas

Do not invent a house style that the user did not ask for.

## 7. Consolidate findings

Use this severity model:

- `Critical`: the business behavior is wrong, contradictory, missing, or too ambiguous to trust
- `High`: the artifact is likely to mislead implementation, review, automation, or sign-off
- `Medium`: a real quality defect with limited reach, such as one weak outcome or a readable but mixed scenario
- `Low`: wording, readability, metadata, or low-risk cleanup

Write the response in this order:

1. findings
2. traceability and coverage notes
3. coaching or rewrite recommendations

If no material defects are present, say so explicitly and move straight to residual gaps or confirmation questions.
