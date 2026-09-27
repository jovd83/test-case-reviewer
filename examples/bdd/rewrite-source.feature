Feature: Discount handling

  Scenario: Gold customer gets a discount
    Given a Gold customer
    When they buy something
    Then a discount is applied

  Scenario: Checkout with discount works
    Given a Gold customer has items in the cart
    When the customer buys a restricted product and checks out
    Then the system handles the result
