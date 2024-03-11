from pages.emag_home_pages import Emag_Home_page
from behave import *

emag_home_pages = Emag_Home_page

@Given('home:I am a user on home page')
def step_impl(context):
    emag_home_pages.navigate_to_emag_home_pages()


@when('home:i click on login button')
def step_impl(context):
    emag_home_pages.click_login_button()



