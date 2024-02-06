from emag_home_page import Home_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import *



class Home_page(Home_page):
    WEBSITE = 'https://www.emag.ro/'
    LOGIN_LINK = 'https://auth.emag.ro/user/login'
    SEARCH_BOX = (By.XPATH, '//*[@id="searchboxTrigger"]')
    ADD_PRODUCTS_IN_CART = (By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[4]/div[2]/form/button')


    def login_link(self):
        account_dropdown = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.LOGIN_LINK))
        self.chrome.find_elements(*self.LOGIN_LINK)

    def search_box(self):
        search_box = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.SEARCH_BOX))
        search_box.send_keys(search_box)

    def add_products_in_cart(self):
        add_products_in_cart = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.ADD_PRODUCTS_IN_CART))
        add_products_in_cart.send_keys(add_products_in_cart)