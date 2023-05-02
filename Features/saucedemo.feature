Feature: QA Assignment | Locale.ai

  Scenario: Verify user is able to login to sauce demo dashboard
    Given User navigates to saucedemo website
    When User enters correct username and password
    And Clicks on login button
    Then User is able to view saucedemo dashboard

  Scenario: Verify user is able to add items to the cart from sauce demo dashboard
    Given User navigates to saucedemo website
    When User enters correct username and password
    And Clicks on login button
    Then User is able to view saucedemo dashboard
    And User is able to add items to cart
    And Verify Count of items in the cart has increased

  Scenario: Verify user is able to checkout and place orders
    Given User navigates to saucedemo website
    When User enters correct username and password
    And Clicks on login button
    Then User is able to view saucedemo dashboard
    And User is able to add items to cart
    And Verify user is able to checkout and add user details during checkout
    And Verify user is able to place order successfully