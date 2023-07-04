import time
from pages.main_page import Main_page
from base.base_class import Base
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Cart_page(Main_page):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    """Locators"""

    parsed_name_in_cart_locator = '//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/a/div/div[1]'
    oformlenie_button = '//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div[2]/div/div/div[3]'
    cart_locator = '//*[@id="__layout"]/div/header/div/div[2]/a'
    nadpis_locator = '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div/h1'


    """Getter"""

    def get_parsed_name_in_cart(self):
        return self.driver.find_element(By.XPATH, self.parsed_name_in_cart_locator)

    def get_oformlenie_button(self):
        return self.driver.find_element(By.XPATH, self.oformlenie_button)

    def get_cart_button(self):
        return self.driver.find_element(By.XPATH, self.cart_locator)

    def get_nadpis_button(self):
        return self.driver.find_element(By.XPATH, self.nadpis_locator)


    """Actions"""

    def check_cart_name(self):
        x = self.get_parsed_name_in_cart().text
        assert x == "Так говорил Заратустра"
        print("Name of product in cart : " + x)
        return x

    def click_oformlenie_button(self):
        self.driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(2)
        self.get_oformlenie_button().click()
        print("Clicked on oformlenie button")

    def open_cart(self):
        self.get_cart_button().click()
        print("Clicked on cart button")
        time.sleep(5)
        assert self.get_nadpis_button() != None
        print("Cart Opened")



