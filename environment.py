from browser import Browser
from pages.emag_home_page import Emag_home_page
from pages.emag_login_page import EmagLoginPage
from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.emag_login_page = EmagLoginPage(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
