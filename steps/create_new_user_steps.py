from behave import *


@given('User can create new account')
def step_impl(context):
    context.emag_home_page.navigate_to_homepage()


@when('The user insert valid credentials {username},{password}')
def step_impl(context,username,password):
    context.emag_create_new_user_page.insert_name(username)
    context.emag_create_new_user_page.insert_password(password)


@when('The user click on the next button')
def step_impl(context):
    context.emag_create_new_user_page.click_next_button()