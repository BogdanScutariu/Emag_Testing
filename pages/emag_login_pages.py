
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *


class EmagLoginPage:
    Email = (By.XPATH, '//*[@id="user_login_email"]')
    Continua = (By.XPATH, '//*[@id="user_login_continue"]')
    Parola = (By.XPATH, '//*[@id="user_login_password"]')
    Continuare = (By.XPATH, '//*[@id="user_login_continue"]')
    Telefon = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/a')
    EroareLogare = (By.XPATH, '//form/div[4]/div/div')

    def email(self, email="email_for_tests@yahoo.com"):
        email_input = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.Email))
        email_input.send_keys(email)

    def continua(self):
        continua_button = WebDriverWait(self.chrome, timeout=3).until(EC.element_to_be_clickable(self.Continua))
        continua_button.click()

    def parola(self, parola="Parola12345"):
        parola_input = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.Parola))
        parola_input.send_keys(parola)

    def continuare(self):
        continuare_button = WebDriverWait(self.chrome, timeout=3).until(EC.element_to_be_clickable(self.Continuare))
        continuare_button.click()

    def telefon(self):
        telefon_link = WebDriverWait(self.chrome, timeout=3).until(EC.element_to_be_clickable(self.Telefon))
        telefon_link.click()

    def check_current_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://www.emag.ro/user/myaccount?ref=ua_personal_data"
        assert expected_url == actual_url, "The URL is incorrect"

    def check_login_error_message(self, expected_error_message):
        self.check_error_message(expected_error_message)

    def check_error_message(self, expected_error_message):
        error_message_web_element = WebDriverWait(self.chrome, timeout=3).until(
            EC.presence_of_element_located(self.EroareLogare))
        actual_error_message_text = error_message_web_element.text
        assert expected_error_message == actual_error_message_text, f'This message is incorrect. Expected: {expected_error_message}'
