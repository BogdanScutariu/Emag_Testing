from behave import *

@Given('User can creat new account')
def step_impl(context):
    context.emag_home_page.navigate_to_emag_home_pages()
    context.emag_home_page.click()


@given('The user insert valid user "{username}" and password "{password}')
def step_impl(context,username,password):
    context.create_new_user_page.insert_name(username)
    context.create_new_user_page.insert_password(password)