Feature: Testing search button from the main page

  Background:
    Given:We will write some random word in search field to see if the button is working

  @T1 @PositiveTesting
  Scenario: Write "Iphone 15" to see if we have corect results
    When Pressing on the field of Search button
    When We write :"Iphone 15"
    When We press search
    Then We should have more page with our product

   @T2 @NegativeTesting
     Scenario: We write "@123456789@" to see if we have a result
      When Pressing on search field
      When We write "@123456789@"
      When We press on search button
      Then We should recive nothing or a text " Searching word has no match