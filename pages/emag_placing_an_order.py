from emag_home_page import Home_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from behave import *


LOGIN_WEBSITE = 'https://www.emag.ro/'
SEARCH_BOX = (By.XPATH, '//*[@id="searchboxTrigger"]')
ADD_PRODUCT_IN_CART = (By.XPATH, '//*[@id="card_grid"]/div[1]/div/div/div[4]/div[2]/form/button')
CHECK_CART = (By.XPATH, '/html/body/div[17]/div/div/div[2]/div/div[3]/a')
CONTINUA = (By.XPATH, '//*[@id="cart-products"]/div/div[2]/div[1]/div/div[2]/div/a')

    def login_website(self):
      account_dropdown = WebDriverWait(self.chrome , timeout=3).until(EC.presence_of_element_located(self.ACCOUNT_DROPDOWN))
      account_dropdown.click()
      self.chrome.find_element(*self.LOGIN_WEBSITE)
      
    def search_box(self, "iphone 15"):
        search_box = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.SEARCH_BOX))
        search_box.send_keys(search_box)


    def add_product_in_cart(self):
        add_product_in_cart = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.ADD_PRODUCT_IN_CART))
        add_product_in_cart.send_keys(add_product_in_cart)

    def check_cart(self):
        check_cart = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.CHECK_CART))
        check_cart.send_keys(check_cart).click()

    def continua(self):
        continua = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.CONTINUA))
        continua.send_keys(continua).click()
