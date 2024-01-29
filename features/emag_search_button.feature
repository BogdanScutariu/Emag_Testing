Feature: Testing search button from the main page

  Background:
    Given:We will write some random word in search field to see if the button is working

  @T1 @PositiveTesting
  Scenario: Wrinte "Iphone 15" to see if we have corect results
    When Pressing on the field of Search button
    When We write :"Iphone 15"
    When We press search
    Then We should have more page with our product