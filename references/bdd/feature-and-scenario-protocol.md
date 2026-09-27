# Feature and Scenario Protocol

Use this file when you need detailed structure rules for features, scenarios, tags, and path coverage.

## Feature rules

- Use one feature file per capability, story-sized behavior group, or coherent rule set.
- Use a feature title that states intent, not a test action.
- Include `As a / I want / So that` when you are creating or rewriting a full feature and the source supports it.
- Split the feature when it becomes too large, mixes unrelated logic, or spans multiple personas without a clear shared goal.

## Scenario rules

- Use one scenario per behavior path.
- Keep one main event in `When`.
- Keep `Given` limited to the context required to understand the behavior.
- State outcomes in `Then` using observable results.
- Use `And` only to continue the same phase.
- Use `But` only when contrast improves clarity.

## Path coverage

Cover these path types when the source material supports them:

- main success path
- alternate but valid path
- error, rejection, or invalid path
- boundary, permission, or lifecycle path when relevant

Path tags like `@main`, `@alt`, and `@error` are optional. Use them only when the project or source material already supports a tagging convention.

## Naming

Use titles that express a condition and an outcome.

Prefer:

```text
Scenario: Gold member receives the standard discount for an eligible product
```

Avoid:

```text
Scenario: Check discount
Scenario: Test 1
Scenario: Happy path
```

## Tags

Use tags only when:

- the project already has a supported tag schema
- the source material explicitly provides tags or IDs
- the user asks for metadata to be preserved

Do not invent:

- requirement IDs
- persona tags
- priority tags
- test-level tags
- automation tags

## `Rule:`

Use `Rule:` when several scenarios belong to one business rule and the rule label improves navigation.

Avoid `Rule:` when it adds ceremony without improving readability.

## `Background:`

Use `Background:` only for context shared by every scenario in the feature.

Good uses:

- a common authenticated state
- a common account or catalog state

Bad uses:

- large hidden setup
- mixed preconditions that apply only to some scenarios

## `Scenario Outline`

Use `Scenario Outline` when:

- each row exercises the same rule shape
- the parameters change the example, not the scenario meaning

Avoid `Scenario Outline` when:

- rows represent unrelated rules
- rows require unrelated expected outcomes
- the outline is being used to compress scenarios that are clearer when written separately

## Example design

- Prefer realistic examples over placeholders.
- Use boundary values when thresholds matter.
- Use state-sensitive examples when lifecycle state changes the outcome.
- Keep vocabulary consistent with the business domain.
