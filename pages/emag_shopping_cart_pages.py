from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from behave import *

class Emag_Home_Page:
    WEBSITE = 'https://www.emag.ro/'
    LOGIN_LINK = (By.LINK_TEXT, 'Intră în cont')
    SEARCH_BOX = (By.XPATH, '//*[@id="searchboxTrigger"]')
    ADD_PRODUCTS_IN_CART = (By.XPATH, '//*[@id="card_grid"]//button[contains(@class, "add-to-cart")]')

    def __init__(self, driver):
        self.driver = driver

    def open_website(self):
        self.driver.get(self.WEBSITE)

    def click_login_link(self):
        login_link = WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(self.LOGIN_LINK))
        login_link.click()

    def search_product(self, product_name):
        search_box = WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_element_located(self.SEARCH_BOX))
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)

    def add_product_to_cart(self):
        add_to_cart_button = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(self.ADD_PRODUCTS_IN_CART))
        add_to_cart_button.click()
