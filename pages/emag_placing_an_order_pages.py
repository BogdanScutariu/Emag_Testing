from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Emag_Home_Page:
    WEBSITE = 'https://www.emag.ro/'
    LOGIN_LINK = (By.LINK_TEXT, 'Intră în cont')
    SEARCH_BOX = (By.XPATH, '//*[@id="searchboxTrigger"]')
    ADD_PRODUCTS_IN_CART = (By.XPATH, '//*[@id="card_grid"]//button[contains(@class, "add-to-cart")]')
    def __init__(self, chrome):
        self.chrome = chrome

    def login_website(self):
        account_dropdown = WebDriverWait(self.chrome, timeout=3).until(
            EC.presence_of_element_located((By.XPATH, '//selector_for_account_dropdown')))
        account_dropdown.click()
        login_link = WebDriverWait(self.chrome, timeout=3).until(
            EC.presence_of_element_located((By.LINK_TEXT, 'Login')))
        login_link.click()

    def search_product(self, product_name):
        search_box = WebDriverWait(self.chrome, timeout=3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="searchboxTrigger"]')))
        search_box.send_keys(product_name + Keys.RETURN)

    def add_product_to_cart(self):
        add_to_cart_button = WebDriverWait(self.chrome, timeout=3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="card_grid"]//form/button')))
        add_to_cart_button.click()

    def check_cart(self):
        check_cart_link = WebDriverWait(self.chrome, timeout=3).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="modal-body"]/div/a')))
        check_cart_link.click()

    def proceed_to_checkout(self):
        continua_link = WebDriverWait(self.chrome, timeout=3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cart-products"]//div[@class="product-details"]/div/a')))
        continua_link.click()
