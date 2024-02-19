from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class EmagHomePage:
    CONT_NOU = (By.XPATH, '//a[@class="btn btn-link btn-sm" and @href="/user/login?ref=hdr_signup_btn"]')
    EMAIL = (By.XPATH, '//*[@id="user_login_email"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="user_login_continue"]')
    NAME_SURNAME = (By.XPATH, '//*[@id="user_register_full_name"]')
    PASSWORD = (By.XPATH, '//*[@id="user_register_password_first"]')
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="user_register_password_second"]')
    CONDITION_BOX_ACCEPT = (By.XPATH, '//label[@for="user_register_agree_terms"]')
    CONTINUA = (By.XPATH, '//*[@id="user_register_continue"]')
    PHONE = (By.CSS_SELECTOR, 'a.text-center.font-weight-semibold[href="/user/authorize"]')

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_homepage(self):
        self.driver.get("https://www.emag.ro/")

    def click_cont_nou(self):
        WebDriverWait(self.driver, timeout=10).until(EC.element_to_be_clickable(self.CONT_NOU)).click()

    def enter_email(self, email="email_for_tests@yahoo.com"):
        email_input = WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(self.EMAIL))
        email_input.send_keys(email)

    def click_continue_button(self):
        continue_button = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        continue_button.click()

    def enter_name_surname(self, name_surname="Ion Ionescu"):
        name_surname_input = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(self.NAME_SURNAME))
        name_surname_input.send_keys(name_surname)

    def enter_password(self, password="Parola12345"):
        password_input = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(self.PASSWORD))
        password_input.send_keys(password)

    def confirm_password(self, password="Parola12345"):
        confirm_password_input = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located(self.CONFIRM_PASSWORD))
        confirm_password_input.send_keys(password)

    def click_condition_box(self):
        condition_box = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(self.CONDITION_BOX_ACCEPT))
        condition_box.click()

    def click_continua_button(self):
        continua_button = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(self.CONTINUA))
        continua_button.click()

    def click_phone_link(self):
        phone_link = WebDriverWait(self.driver, timeout=10).until(
            EC.element_to_be_clickable(self.PHONE))
        phone_link.click()

    def check_current_url(self):
        actual_url = self.driver.current_url
        expected_url = "https://www.emag.ro/"
        assert actual_url == expected_url, f"The current URL {actual_url} is not as expected."
