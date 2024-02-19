from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class EmagHomePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_homepage(self):
        self.driver.get("https://www.emag.ro/")

class EmagCreateNewUserPage:
    NAME_INPUT = (By.ID, 'name')
    PASSWORD_INPUT = (By.ID, 'password')
    NEXT_BUTTON = (By.ID, 'next_button')

    def __init__(self, driver):
        self.driver = driver

    def insert_name(self, name):
        name_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NAME_INPUT))
        name_input.clear()
        name_input.send_keys(name)

    def insert_password(self, password):
        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

    def click_next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.NEXT_BUTTON))
        next_button.click()
