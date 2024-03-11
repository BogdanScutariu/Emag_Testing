from behave import *

@given('The user is on main page')
def step_impl(context):
    context.emag_login_page.navigate_to_homepage()

@when('We click on login button')
def step_impl(context):
    context.emag_login_page.click_login_button()

@then('We are logged into website')
def step_impl(context):
    context.emag_login_page.check_current_url()

@then('The user receives an error message {error_message} and cannot log in')
def step_impl(context, error_message):
    context.emag_login_page.check_error_message(error_message)

@when('We insert username {} and password {password}')
def step_impl(context, username, password):
    context.emag_login_page.insert_username(username)
    context.emag_login_page.insert_password(password)

