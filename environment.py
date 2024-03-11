from browser import Browser
from selenium import webdriver
from pages.emag_login_pages import EmagLoginPage

def before_all(context):
    context.driver = webdriver.Chrome()
    context.browser = Browser()
    context.emag_login_page = EmagLoginPage()


def after_scenario(context, scenario):
    context.driver.quit()
