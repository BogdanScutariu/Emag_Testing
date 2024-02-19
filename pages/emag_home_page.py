from selenium import webdriver
import time
from webdriver_manager.core import driver

Home_page = webdriver.Chrome()
Home_page.get("https://www.emag.ro/")
Home_page.maximize_window()
time.sleep(5)
