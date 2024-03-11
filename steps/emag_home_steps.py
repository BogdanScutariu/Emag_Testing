from pages.emag_home_page import Emag_Home_page
from behave import *

emag_home_page = Emag_Home_page

@Given('home:I am a user on home page')
def step_impl(context):
    emag_home_page.navigate_to_emag_home_pages()


@when('home:i click on login button')
def step_impl(context):
    emag_home_page.click_login_button()



