import self

from emag_home_page import Home_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from webdriver_manager.core import driver
class Add_user_page(Home_page):
    CONT_NOU = (By.XPATH, "/html/body/div[10]/div/div[2]/a[2]")
    EMAIL = (By.XPATH, '//*[@id="user_login_email"]')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="user_login_continue"]')
    NAME_SURNAME = (By.XPATH, '//*[@id="user_register_full_name"]')
    PASSWORD = (By.XPATH, '//*[@id="user_register_password_first"]')
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="user_register_password_second"]')
    CONDITION_BOX_ACCEPT = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/form/div[7]/div[1]/label')
    CONTINUA = (By.XPATH, '//*[@id="user_register_continue"]')
    PHONE = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/a')

    def navigate_to_homepage(self):
        self.chrome.get("https://www.emag.ro/")

    def cont_nou(self):
        cont_nou = WebDriverWait(self.chrome, timeout=3).until(EC.element_to_be_clickble(self.CONT_NOU))
        self.chrome.find_element(*self.CONT_NOU).click()
    def email(self,email="email_for_tests@yahoo.com"):
        email = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.EMAIL))
        email.send_keys(email)

    def continue_button(self):
         continue_button = WebDriverWait(self.chrome, timeout=3).until(EC.element_to_be_clickble(self.CONTINUE_BUTTON))
         self.chrome.find_element(*self.CONTINUE_BUTTON).click()

    def name_surname(self, name_surname = "Ion Ionescu" ):
        name_surname = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.NAME_SURNAME))
        name_surname.send_keys(name_surname)

    def password(self, password = "Parola12345"):
        password = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.PASSWORD))
        self.chrome.find_element(*self.PASSWORD).send_keys(password)

    def confirm_password(self, password = "Parola12345"):
        confirm_password = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.CONFIRM_PASSWORD))
        self.chrome.find_element(*self.CONFIRM_PASSWORD).send_keys(password)
    def condition_box_accepted(self):
         condition_box_accepted = WebDriverWait(self.chrome, timeout=3).until(EC.element_to_be_clickble(self.CONDITION_BOX_ACCEPT))
         self.chrome.find_element(*self.CONDITION_BOX_ACCEPT).click()

    def continua(self):
        continua = WebDriverWait(self.chrome, timeout=3).until(
            EC.element_to_be_clickble(self.CONTINUA))
        self.chrome.find_element(*self.CONTINUA).click()

    def phone(self):
        phone = WebDriverWait(self.chrome, timeout=3).until(
            EC.element_to_be_clickble(self.PHONE))
        self.chrome.find_element(*self.PHONE).click()


    def check_current_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://www.emag.ro/"
