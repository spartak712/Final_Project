import time

from base.base_class import Base
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    search_field = '//*[@id="__layout"]/div/header/div/div[1]/div[2]/div[1]/form/input[1]'
    Nietze_checkbox = '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/div/section/ul/li[4]/div/div[2]/div[3]/ul/li[1]/label/div'
    izdatel_checkbox = '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/div/section/ul/li[6]/div/div[2]/div[3]/ul/li[3]/label/div'
    noir_korzina = '//*[@id="content-wrap"]/div[2]/div/div/div[2]/div[2]/div[1]/a/div[9]/div/div/button[2]/span/span'
    add_button = '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/section/section/div/article[2]/div[3]/div[1]/span'
    parsed_name_in_catalog_locator = '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/section/section/div/article[2]/div[2]/a/div/div[1]'


    """Getter"""

    def get_search_field(self):
        return self.driver.find_element(By.XPATH, self.search_field)

    def get_Nietze_checkbox(self):
        return self.driver.find_element(By.XPATH, self.Nietze_checkbox)

    def get_izdatel_checkbox(self):
        return self.driver.find_element(By.XPATH, self.izdatel_checkbox)

    def get_parsed_name_in_catalog(self):
        return self.driver.find_element(By.XPATH, self.parsed_name_in_catalog_locator)

    def get_add_button(self):
        return self.driver.find_element(By.XPATH, self.add_button)





    """Actions"""

    def click_search_field(self):
        self.get_search_field().click()
        print("Search field Clicked")

    def input_name_of_product(self, name_of_product):
        self.get_search_field().send_keys(name_of_product)
        self.get_search_field().send_keys(Keys.RETURN)
        print("Name of product added in search field")

    def add_Nietze_checkbox(self):
        self.driver.execute_script("window.scrollTo(0, 700)")
        time.sleep(2)
        self.get_Nietze_checkbox().click()
        print("Clicked on Nietze checkbox")

    def add_izdatel_checkbox(self):
        self.driver.execute_script("window.scrollTo(0, 1200)")
        time.sleep(2)
        self.get_izdatel_checkbox().click()
        print("Clicked on izdatel checkbox")

    def check_catalog_name(self):
        self.driver.execute_script("window.scrollTo(0, 500)")
        time.sleep(2)
        x = self.get_parsed_name_in_catalog().text
        assert x == "Так говорил Заратустра"
        print("Name of product in catalog : " + x)
        return x

    def click_add_button(self):
        self.driver.execute_script("window.scrollTo(0, 300)")
        time.sleep(2)
        self.get_add_button().click()
        print("Clicked on add button")

