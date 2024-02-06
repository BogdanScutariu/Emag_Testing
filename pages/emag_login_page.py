from emag_home_page import Home_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from emag_home_page import Home_page


class Emag_login_page:
    pass


class Login_page(Emag_login_page):
    Email = (By.XPATH, '//*[@id="user_login_email"]')
    Continua = (By.XPATH, '//*[@id="user_login_continue"]')
    Parola = (By.XPATH, '//*[@id="user_login_password"]')
    Continuare = (By.XPATH, '//*[@id="user_login_continue"]')
    Telefon = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/a')
    Eroare_logare =(By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[4]/div/div')

    def email(self,email="email_for_tests@yahoo.com"):
        email = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.Email))
        email.send_keys(email)

    def continua(self):
        continua = WebDriverWait(self.chrome, timeout=3).until(EC.element_to_be_clickble(self.Continua))
        self.chrome.find_element(*self.Continua).click()


    def parola(self,parola="Parola12345"):
        parola = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(self.Parola))
        parola.send_keys(parola)

    def continuare(self):
        continuare = WebDriverWait(self.chrome, timeout=3).until(EC.element_to_be_clickble(self.Continuare))
        self.chrome.find_element(*self.Continuare).click()


    def telefon(self):
        telefon = WebDriverWait(self.chrome, timeout=3).until(EC.element_to_be_clickble(self.Telefon))
        self.chrome.find_element(*self.Telefon).click()

    def check_current_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://www.emag.ro/user/myaccount?ref=ua_personal_data"
        assert expected_url == actual_url , "The url is incorrect"


    def check_login_error_message(self, expected_error_message):
        self.check_error_message(*self.Eroare_logare, expected_error_message)


    def check_error_message(self, by, selector, expected_error_message):
        error_message_web_element = WebDriverWait(self.chrome, timeout=3).until(EC.presence_of_element_located(
            self.Eroare_logare
        ))
        actual_error_message_text = error_message_web_element.text

        assert  expected_error_message == actual_error_message_text, f'This message is incorect. Expected:{actual_error_message_text}'

        presence_of_element_located(By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[4]/div/div')