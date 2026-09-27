# Test Case Quality Examples

Use this reference when you need concrete examples to judge quality, explain a finding, or mentor the test author. The examples below use a consistent quality ladder from very weak to excellent.

## Contents

1. Very Weak Example: No Context
2. Very Weak Example: Generic Error Case
3. Weak Example: Code-Mirroring Oracle
4. Weak Example: Missing Negative Coverage
5. Weak Example: Weak Preconditions
6. Moderate Example: Descriptive but Incomplete
7. Good Example: Clear Manual Case
8. Good Example: Boundary-Focused Case
9. Very Good Example: Strong Business Rule Coverage
10. Excellent Example: Review-Ready Case

## 1. Very Weak Example: No Context

### Draft

- Title: `test login`
- Preconditions: none
- Steps: `login`
- Expected result: `works`

### Why It Is Bad

- no requirement or suite context
- no setup state
- no executable step detail
- no observable expected result
- impossible to trace or automate safely

### Better Direction

- identify the actor, input, and expected UI or API response
- state the login state before execution
- use a descriptive title with path classification

## 2. Very Weak Example: Generic Error Case

### Draft

- Title: `error test`
- Preconditions: `system on`
- Steps:
  - `enter wrong stuff`
- Expected result: `error`

### Why It Is Bad

- invalid input is undefined
- error outcome is too vague
- no business rule or oracle reference
- not reproducible

### Better Direction

- name the invalid input explicitly
- name the expected validation message or rejection code
- tie the case to a requirement or acceptance criterion

## 3. Weak Example: Code-Mirroring Oracle

### Draft

- Title: `TC03 calculate discount`
- Preconditions:
  - `service is deployed`
- Steps:
  - `send discount request with vip=true`
- Expected result:
  - `discount is 12 because that is what the service returns now`

### Why It Is Bad

- expected result is based on current implementation behavior
- no approved business oracle
- likely to create green-but-wrong tests

### Better Direction

- cite the pricing rule or acceptance criterion
- explain why the discount should be 12
- add boundary and non-vip comparisons if the rule depends on status

## 4. Weak Example: Missing Negative Coverage

### Draft

- Title: `UC05 TC01: MSS - transfer succeeds`
- Preconditions:
  - `user is logged in`
  - `source account has 500 EUR`
- Steps:
  - `transfer 100 EUR to target account`
- Expected result:
  - `transfer succeeds`
  - `balance is updated`

### Why It Is Weak

- only the happy path is covered
- insufficient funds, blocked account, and invalid amount are not tested
- expected result is still too generic

### Better Direction

- add ERR and EXT scenarios
- specify the exact source and target balances
- state the transfer status or confirmation message

## 5. Weak Example: Weak Preconditions

### Draft

- Title: `UC09 TC02: ERR - reset password fails`
- Preconditions:
  - `user exists`
- Steps:
  - `reset password`
- Expected result:
  - `reset is denied`

### Why It Is Weak

- denial reason is unclear
- missing trigger condition such as expired token or reused token
- missing observable outcome

### Better Direction

- define the exact failing condition
- describe the request channel and token state
- assert the specific error message and unchanged password state

## 6. Moderate Example: Descriptive but Incomplete

### Draft

- Title: `UC12 TC03: ERR - withdrawal rejected when amount exceeds daily limit`
- Preconditions:
  - `customer is authenticated`
  - `customer daily withdrawn amount is 450 EUR`
  - `daily limit is 500 EUR`
- Steps:
  - `request withdrawal of 100 EUR`
- Expected result:
  - `withdrawal is rejected`

### What Is Good

- descriptive title
- realistic numbers
- clear error condition

### What Is Missing

- no explicit oracle reference
- no expected rejection code or message
- no assertion that balance and audit trail remain correct

### Better Direction

- tie the case to the withdrawal limit requirement
- assert balance unchanged, rejection reason shown, and event logged if required

## 7. Good Example: Clear Manual Case

### Draft

- Title: `UC12 TC04: ERR - withdrawal rejected when amount exceeds daily limit`
- Preconditions:
  - `A. Customer is authenticated in ATM session`
  - `B. Customer account balance is 1200 EUR`
  - `C. Customer has already withdrawn 450 EUR today`
  - `D. Daily withdrawal limit is 500 EUR`
- Steps:
  - `1. Enter withdrawal amount 100 EUR`
  - `2. Confirm the withdrawal request`
- Expected result:
  - `1. The ATM rejects the transaction`
  - `2. The message "Daily withdrawal limit exceeded" is shown`
  - `3. Account balance remains 1200 EUR`

### Why It Is Good

- strong setup
- executable steps
- observable expected results
- easy to review and automate later

### What Could Improve It

- add the requirement ID
- add test level or priority if the project uses it

## 8. Good Example: Boundary-Focused Case

### Draft

- Title: `REQ-44 TC06: MSS - premium shipping remains available at basket total 49.99 EUR`
- Preconditions:
  - `A. Premium shipping threshold is 50.00 EUR`
  - `B. Customer basket contains valid in-stock items totaling 49.99 EUR`
- Steps:
  - `1. Open checkout`
- Expected result:
  - `1. Premium shipping is not offered`
  - `2. Standard shipping is offered`

### Why It Is Good

- clear boundary condition
- exact numeric value
- expected behavior is testable

### What Could Improve It

- pair it with adjacent tests at 50.00 EUR and 50.01 EUR
- include requirement wording if ambiguity exists

## 9. Very Good Example: Strong Business Rule Coverage

### Draft

- Title: `REQ-18 TC08: EXT - loyalty discount applied when customer is gold and coupon is absent`
- Preconditions:
  - `A. Pricing rule REQ-18 states that gold customers receive a 10 percent loyalty discount when no coupon overrides the offer`
  - `B. Customer status is Gold`
  - `C. Basket subtotal is 200 EUR`
  - `D. No coupon is applied`
- Steps:
  - `1. Open order summary`
  - `2. Finalize pricing`
- Expected result:
  - `1. Loyalty discount line is shown`
  - `2. Discount amount is 20 EUR`
  - `3. Final price is 180 EUR`
  - `4. No coupon discount line is shown`

### Why It Is Very Good

- explicit oracle
- clear business condition
- numeric assertions
- verifies both applied and not-applied behavior

## 10. Excellent Example: Review-Ready Case

### Draft

- Title: `UC21 TC11: ERR - payment authorization is rejected when 3-D Secure challenge expires before confirmation`
- Preconditions:
  - `A. UC21 and AC-21.4 require the payment to fail when the 3-D Secure challenge is not confirmed within 5 minutes`
  - `B. Customer is authenticated and has items in basket`
  - `C. Payment gateway sandbox is available`
  - `D. Test card supports 3-D Secure challenge flow`
  - `E. Challenge is started at 10:00 and no confirmation is submitted before 10:05`
- Steps:
  - `1. Submit order with the 3-D Secure test card`
  - `2. Wait until the challenge expires`
  - `3. Return to the merchant site`
- Expected result:
  - `1. Payment status is Rejected`
  - `2. Order is not created`
  - `3. Customer sees the message "Authentication timed out. Please try again."`
  - `4. Basket contents remain unchanged`
  - `5. Audit entry records timeout rejection reason`

### Why It Is Excellent

- explicit oracle and timing rule
- realistic system dependencies
- precise stateful path
- strong observable outcomes across UI, domain state, and audit behavior
- ready for review, execution, and automation mapping
