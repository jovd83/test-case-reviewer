# Quality Ladder Examples

This file gives five graded examples from very bad to strong. Each example shows representative input and the expected style of output from the skill.

## 1. Very bad review target

### Input

```text
Review this scenario:

Scenario: Test login
  Given I click the login field
  And I type bob
  And I type secret
  When I click the button
  Then it works
```

### Expected output

```text
Mode: review
Oracle used: scenario text only
Oracle sufficiency: weak
Confidence: low

Findings:
1. High: The scenario is a UI script rather than business-readable behavior.
   Evidence: "I click the login field", "I click the button"
   Why it matters: The scenario will not serve as durable business documentation.
   Fix: Rewrite the steps in domain language around sign-in behavior.
2. High: The expected result is vague.
   Evidence: "Then it works"
   Why it matters: The outcome is not verifiable.
   Fix: Replace it with an observable result such as access to the dashboard.
3. Low: The title is too generic.
   Evidence: "Scenario: Test login"
   Why it matters: It does not describe the condition and the outcome.
   Fix: Rename it to reflect the user behavior and result.
```

## 2. Weak feature draft

### Input

```text
Review this feature:

Feature: Discounts
  Scenario: customer gets discount and checkout succeeds
    Given a customer exists
    When the customer buys a product
    Then the discount is correct
    And the order is confirmed
```

### Expected output

```text
Mode: review
Oracle used: feature text only
Oracle sufficiency: weak
Confidence: low

Findings:
1. High: The scenario combines multiple behaviors.
   Evidence: discount calculation and order confirmation appear in the same scenario.
   Why it matters: Mixed behaviors make coverage and maintenance harder.
   Fix: Split discount calculation and checkout confirmation into separate scenarios if they represent different rules.
2. High: The expected outcome is vague.
   Evidence: "Then the discount is correct"
   Why it matters: The scenario does not say what correct means.
   Fix: Use a concrete amount, rate, or business outcome.
3. Low: The feature title is too broad.
   Evidence: "Feature: Discounts"
   Why it matters: The scope is unclear.
   Fix: Rename the feature around a specific capability or rule set.
```

## 3. Rewrite request

### Input

```text
Rewrite this scenario:

Scenario: Gold customer gets discount
  Given a Gold customer
  When they buy something
  Then a discount is applied
```

### Expected output

```text
Mode: rewrite
Rewrite strategy:
- Preserve the core discount rule.
- Replace vague nouns and outcomes with a concrete business example.

Rewritten artifact:
Scenario: Gold member receives the standard discount for an eligible product
  Given a Gold member with an active subscription
  When the member buys an eligible product
  Then the checkout total includes the standard Gold discount

Open assumptions:
- The exact discount rate was not provided.
- Eligibility rules for restricted products were not provided.
```

## 4. Hybrid review and rewrite

### Input

```text
Review and improve this feature against the acceptance criteria for password reset.
```

### Expected output

```text
Mode: hybrid
Oracle used: acceptance criteria
Oracle sufficiency: partial
Confidence: medium

Key findings:
1. High: Coverage is missing the expired-link rejection path.
2. High: The main scenario does not state an externally visible post-reset result.

Rewritten artifact:
Feature: Password reset by registered user
  As a registered user
  I want to reset my password
  So that I can regain access to my account

  Scenario: Registered user resets a password with a valid reset link
    Given a registered user requested a password reset
    When the user opens a valid reset link and submits a new password
    Then the password is updated
    And the user can sign in with the new password

  Scenario: Registered user cannot reset a password with an expired reset link
    Given a registered user requested a password reset
    And the reset link is expired
    When the user opens the expired reset link
    Then the user sees a message that the reset link is no longer valid

Open assumptions:
- The criteria do not define whether requesting a second reset link invalidates the first link.
```

## 5. Strong review target

### Input

```text
Review this feature for BDD quality and coverage:

@requirement-PWD-101
Feature: Password reset
  As a registered user
  I want to reset my password
  So that I can regain access to my account

  @main
  Scenario: Registered user resets a password with a valid reset link
    Given a registered user requested a password reset
    When the user opens a valid reset link and submits a new password
    Then the password is updated
    And the user can sign in with the new password

  @error
  Scenario: Registered user cannot reset a password with an expired reset link
    Given a registered user requested a password reset
    And the reset link is expired
    When the user opens the expired reset link
    Then the user sees a message that the reset link is no longer valid
```

### Expected output

```text
Mode: review
Oracle used: feature text and requirement tag
Oracle sufficiency: partial
Confidence: medium

Findings:
- No material defects identified.

Traceability and coverage:
- The main and expired-link rejection paths are clear and business-readable.
- Additional alternate-path behavior should only be added if the source requirements define it.

Top recommendations:
- Confirm whether resend-link behavior is in scope before expanding the feature.
```
