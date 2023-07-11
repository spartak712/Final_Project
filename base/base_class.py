import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Base():


    def __init__(self, driver):
        self.driver = driver


    """Method for open full browser"""
    def open_browser(self, url):
        browser = self.driver
        browser.get(url)
        browser.maximize_window()


    """Method for getting current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL : " + get_url)


    """Method for doing screenshot in finish"""
    def get_screen(self, name_of_test):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot_" + name_of_test + "_" + now_date + ".png"
        self.driver.save_screenshot('..\\screens\\' + name_screenshot)
        print("Screen done!")
