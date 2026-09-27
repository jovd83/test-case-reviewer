# BDD Quality Rules

Use this file for detailed review criteria, rewrite heuristics, and anti-pattern correction moves.

## Core checklist

Confirm these when possible:

- the business rule is clear
- the scenario describes one behavior path
- `Given`, `When`, and `Then` are used with clear intent
- the steps are written at the business level
- the outcome is observable from outside the system
- the wording is concrete and domain-specific
- a stakeholder can understand the scenario
- a developer can implement the intended behavior from it
- a tester can verify it without guessing

## Strong patterns

### Concrete examples

Prefer:

```gherkin
Given a Gold member with an active subscription
When the member buys an eligible product
Then the checkout total includes the standard Gold discount
```

Avoid:

```gherkin
Given a <customerType>
When the user buys an <item>
Then the system handles the discount
```

### Single-responsibility scenario

Keep one scenario focused on one rule branch or one outcome.

### Business-focused language

Use the terms stakeholders use. Remove technical nouns unless they are part of the business domain.

### Observable outcomes

Write results that a user, tester, or external observer can verify directly.

### Minimal `Given`

Keep only the context needed to understand the action and the result.

## Common anti-patterns

### UI script in disguise

Avoid:

```gherkin
Given I click the login button
And I enter my username
And I click submit
```

### Multiple meaningful events

Avoid multiple user actions that each change the scenario's purpose.

### Branching inside one scenario

Avoid mixed alternate outcomes or conditional language inside a single scenario.

### Vague outcomes

Avoid:

```gherkin
Then it works
Then the request succeeds
Then the result is correct
```

### Invisible outcomes

Avoid using logs, internal tables, selectors, or implementation details as the primary result unless the user explicitly asks for internal verification.

### Generic data

Avoid placeholders when a concrete example would explain the rule better.

### Background abuse

Avoid moving large amounts of hidden setup into `Background:`.

## Correction moves

Use these fixes directly:

- UI-scripted step -> rewrite in business language
- vague `Then` -> replace with observable result
- overloaded scenario -> split into separate scenarios
- generic title -> rename with condition and outcome
- missing path coverage -> add supported main, alternate, or error scenarios
- weak example data -> replace with realistic values

## Confidence rule

Quality problems can be assessed even when correctness cannot.

If the oracle is weak:

- critique structure, clarity, and BDD quality
- lower confidence
- avoid claiming the scenario is behaviorally correct
