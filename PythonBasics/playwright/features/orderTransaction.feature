Feature: Order Transaction
  Tests related to Order Transaction

  Scenario Outline: Verify Order success message shown in details page
    Given place the item order as user <user_index>
    And the user is on the landing page
    When I login to portal as user <user_index>
    And navigate to orders page
    And  select the orderId
    Then the order message is successfully displayed
    Examples:
    | user_index |
    | 0          |
