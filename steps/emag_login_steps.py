from behave import *


@given('The user is on main page')
def step_impl(context):
    context.emag_login_page.navigate_to_homepage()
    #context.emag_login_page.accept_cookies()


#context.emag_login_page.insert_username(username)
#context.emag_login_page.insert_password(password)

@when('We click on login button')
def step_impl(context):
    context.emag_login_page.click_login_button()


@then('We are logged into website')
def step_impl(context):
    #raise NotImplementedError('Then the user is logged into website')
    context.emag_login_page.check_curent_url()


@then('The user recive a error message {error_message} and cannot login to weite')
def step_impl(context,error_message):
    context.emag_login_page.check_error_message(error_message)

#raise NotImplementedError('Then the user recive a error message:"invalid credentials and cannot login to website')

@when('We insert username{email_for_tests@yahoo.com} and password{Parola12345}')
def step_impl(context, username,password):
    try:context.emag_login_page.logout_of_the_website()
    except:pass
    context.emag_login_page.insert_username(username)
    context.emag_login_page.insert_password(password)


@given('The user is logged in succesfully')
def ste_impl(context):
    context.emag_login_page.insert_username()
    context.emag_login_page.insert_password()

