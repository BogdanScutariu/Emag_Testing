from selenium import webdriver
from selenium import webdriver
import time
from webdriver_manager.core import driver

Home_page = webdriver.Chrome()
Home_page.get("https://www.emag.ro/")
Home_page.maximize_window()
time.sleep(5)



from selenium import webdriver

class Browser:
    def __init__(self):
        self.chrome = webdriver.Chrome()

    def maximize_browser(self):
        self.chrome.maximize_window()

    def close_browser(self):
        self.chrome.quit()
