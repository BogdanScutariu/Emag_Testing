Feature: We verify if we can place a order succesfully

  Background: The user navigate to main page

    @Oder
    Scenario: Login and placind an order
      When We insert our credentials
      When We search for Iphone 13 "
      When We add the product in shopping cart
      When We click on "Place order"
      Then The order is placed and we recive a order number