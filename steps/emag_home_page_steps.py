from selenium.webdriver.chrome.webdriver import WebDriver
from pages.emag_home_page import Emag_home_page
from behave import *

Emag_home_page = emag_home_page()

@given('home:I`m user on home page')
def step_impl(context):
    emag_home_page.navigate_to_homepage()

@when('home: We click login button')
def step_impl(context):
    emag_home_page.click_login_button()
