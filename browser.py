from selenium import webdriver




class Browser():
    chrome = webdriver.Chrome()

    def maximise_browser(self):
        self.chrome.maximize_window()


    def close_browser(self):
        self.chrome.quit()