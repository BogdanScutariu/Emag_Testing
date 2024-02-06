from pages.emag_home_page import Home_page
from behave import *

home_page = Home_page

@given('home:I`m user on home page')
def step_impl(context):
    home_page.navigate_to_homepage()


@when('home: We click login button')
def step_impl(context):
    home_page.click_login_button()

