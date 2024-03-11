from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager import chrome
from pages.create_new_user_pages import Emag_Home_Page
from browser import Browser


class Emag_Home_page():
    def navigate_to_Emag_home_pages(self):
        self.chrome.get("https://www.emag.ro/")

    def logout_of_the_website(self):
        account_dropdown = WebDriverWait(self.chrome, timeout=10).until(
            EC.presence_of_element_located(self.ACCOUNT_DROPDOWN))
        account_dropdown.click()
