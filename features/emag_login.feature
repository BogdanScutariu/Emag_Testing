Feature: We check that the login functionality of the website in working
  Background:
    Given Username button is on the "Emag.ro" main page


    @T1 @PositiveTesting
  Scenario: Check if we can login succesfully with our credentials
      When We enter valid email and valid password
      When We click on login button
      Then Login is succesfuly done


     @T2 @NegativeTesting
  Scenario: We check if we can login with invalid unsername and valid password
       When We insert invalid username and valid password
       When We press login button
       Then Login failed and we recive a message" Invalid username or password"


     @T3 @NegativeTesting
  Scenario: Check if we can login with valid email and invalid password
       When We insert valid email and invalid password
       When We press the login button
       Then Login failed: "Invalid username or password"


     @T4 @NegativeTesting
  Scenario: Checking if login is possible with invalid email and invalid password
       When We write invalid email and invald password
       When We press Login button
       Then We recive a error message "Invalid user or password"

     @T5 @NegativeTesting
  Scenario Outline: Check if the user can login with invalid credentials
       When We insert username "<username>" and password "<password>"
       When We press login button
       Then We recive error with a message:"Username or password incorect"
       Examples:
       |username|password|
       |Testuser|testpassord|
       |Testuser1|Testpass  |
       |Admin    |Admin234  |
       |username |password  |

     @T6 @PositiveTesting
  Scenario Outline: Check if the user can login with invalid credentials and we should recive a message "invalid username or password"
       When We insert username "<username>" and password "<password>"
       When We press login button
       Then We recive error with a message:"Username or password incorect"
       Examples:
       | username | password | Error message |
       | Testuser | testpassword| Invalid username or password|
       | Testuser1| Testpass  | Invalid username or password|
       | Admin    | Admin234  | Invalid username or password|
       | username | password  |  Invalid username or password|