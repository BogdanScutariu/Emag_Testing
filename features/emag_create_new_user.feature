Feature: Complete and verify functionalities for creating a new user

    Background:
      Given User can create new account

      @T1 @PositiveTesting
    Scenario: Chech if we can enter email adress and a password
        When User insert valid email adress "email_for_tests" and password "Parola12345"
        When I write name and surname
        When We click on next button
        Then Account is succesfully created

       @T2 @NegativeTesting
    Scenario: Check if the user can create a user with invalid credentials
         When The user insert corect email and corect password
         When The user leave the fields for name and surname empty
         When User press next button
         Then We recive a Error with a message:"You must fill the mandatory fields"