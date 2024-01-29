from browser import Browser
from pages.add_user_page import Add_user_page

from page.home_page import Home_page
from page.login_page import Login_page

def before_all(context):
    context,browser = Browser()
    context.login_page = Login_page()
    context.home_page = Home_page()
    context.add_user_page = Add_user_page()
    context.browser.maximise_windows()

def after_all(context):
    context.browser.close_browser()