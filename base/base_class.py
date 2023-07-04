import datetime

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

    def get_screen(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\Spartak\\Desktop\\WORK\\Test_Project\\screens\\' + name_screenshot)
        print("Screen done!")
