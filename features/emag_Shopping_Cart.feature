Feature:  We check the functionality of shopping cart

  Background:
    Given Navigate to Shopping cart page


   @Shopping
   Scenario: Adding one intem in shopping cart
     When We add one item to our shopping cart
     Then Count of item from shopping cart is one

   @Shopping
   Scenario: We add multiple products in our cart
     When We add multiple product in our shopping cart
     Then There are multiple products in our shopping cart


   @Shopping
   Scenario: We want to remove a product from our cart
     When We add more product in our cart
     When We click on our cart
     When We click on product that we want to remove
     Then Product is removed