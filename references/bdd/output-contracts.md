# Output Contracts

Use these response shapes when the request needs a more explicit structure than the default skill flow.

## Review contract

```text
Mode: review
Oracle used: <sources>
Oracle sufficiency: <strong|partial|weak>
Confidence: <high|medium|low>

Findings:
1. <Severity>: <issue>
   Evidence: <scenario, step, or requirement>
   Why it matters: <impact>
   Fix: <recommended correction>

Traceability and coverage:
- <summary>

Top recommendations:
- <action>
```

Use `Confidence: low` when the source of truth is weak or missing.

If no material defects are found, replace the findings list with:

```text
Findings:
- No material defects identified.
```

Then list any residual questions or optional improvements.

## Rewrite contract

```text
Mode: rewrite
Rewrite strategy:
- <what changed and why>

Rewritten artifact:
<gherkin>

Open assumptions:
- <gap, unresolved rule, or missing metadata>
```

## Generate contract

```text
Mode: generate
Source inputs:
- <artifact type>

Generated artifact:
<gherkin>

Assumptions and gaps:
- <unsupported behavior or missing decision>
```

## Hybrid contract

```text
Mode: hybrid
Oracle used: <sources>
Oracle sufficiency: <strong|partial|weak>
Confidence: <high|medium|low>

Key findings:
1. <Severity>: <issue>

Rewritten artifact:
<gherkin>

Open assumptions:
- <item>
```

## Insufficient-oracle fallback

Use this shape when the user asks for correctness judgment but the source material is too weak:

```text
Mode: <review|hybrid>
Oracle used: <sources>
Oracle sufficiency: weak
Confidence: low

Limitations:
- <what cannot be confirmed>

BDD quality findings:
1. <Severity>: <issue>

Blocked decisions:
- <missing rule or ambiguity>
```

## Formal report contract

Use [../../assets/bdd-review-report-template.md](../../assets/bdd-review-report-template.md) when the user explicitly asks for:

- a formal review report
- an executive summary
- a scorecard
- coaching recommendations in report form
