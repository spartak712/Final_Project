import time
from pages.main_page import Main_page
from base.base_class import Base
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class Cart_page(Main_page):


    """Locators"""

    parsed_name_in_cart_locator = '//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/a/div/div[1]'
    parsed_avtor_in_cart_locator = '//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div[1]/div/div/div[2]/div/div/div[1]/a/div/div[2]'
    oformlenie_button = '//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div[2]/div/div/div[3]'
    cart_locator = '//*[@id="__layout"]/div/header/div/div[2]/a'
    nadpis_locator = '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div/h1'
    number_field_locator = '//*[@id="__layout"]/div/div[5]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/label/input'



    """Getters"""

    def get_parsed_name_in_cart(self):
        return self.driver.find_element(By.XPATH, self.parsed_name_in_cart_locator)

    def get_parsed_avtor_in_cart(self):
        return self.driver.find_element(By.XPATH, self.parsed_avtor_in_cart_locator)

    def get_oformlenie_button(self):
        return self.driver.find_element(By.XPATH, self.oformlenie_button)

    def get_cart_button(self):
        return self.driver.find_element(By.XPATH, self.cart_locator)

    def get_nadpis_button(self):
        return self.driver.find_element(By.XPATH, self.nadpis_locator)

    def get_number_field(self):
        return self.driver.find_element(By.XPATH, self.number_field_locator)



    """Actions"""

# Открывает корзину
    def open_cart(self):
        self.get_cart_button().click()
        print("Clicked on cart button")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.nadpis_locator)))
        # assert self.get_nadpis_button() != None
        print("Cart Opened")


# Парсит название книги в корзине
    def check_name_in_cart(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.parsed_avtor_in_cart_locator)))
        x = self.get_parsed_name_in_cart().text
        assert x == "Так говорил Заратустра"
        print("Name of product in cart : " + x)
        return x


# Парсит имя автора в корзине
    def check_avtor_name_in_cart(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.parsed_name_in_cart_locator)))
        x = self.get_parsed_avtor_in_cart().text
        assert x == "Фридрих Ницше"
        print("Author's name in cart : " + x)
        return x


# Оформляет покупку
    def click_oformlenie_button(self):
        self.driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(1)
        self.get_oformlenie_button().click()
        print("Clicked on oformlenie button")


# Вводит номер в поле
    def input_number(self, number):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.number_field_locator)))
        self.get_number_field().send_keys(number)
        self.get_number_field().send_keys(Keys.RETURN)
        print("Number added : " + number)


# Проделывает основные шаги страницы корзины по тесту test_buy_zaratustra
    def parsing_chosen_data(self):
        spisok = [""]
        self.open_cart()
        x = self.check_name_in_cart()
        spisok.append(x)
        time.sleep(1)
        i = self.check_avtor_name_in_cart()
        spisok.append(i)
        return spisok






