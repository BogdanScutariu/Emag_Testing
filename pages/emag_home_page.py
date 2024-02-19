from selenium import webdriver
import time
from webdriver_manager.core import driver

Emag_home_page = webdriver.Chrome()
Emag_home_page.get("https://www.emag.ro/")
Emag_home_page.maximize_window()
time.sleep(5)
