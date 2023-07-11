import time

from base.base_class import Base
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Main_page(Base):


    """Locators"""

    search_field = '//*[@id="__layout"]/div/header/div/div[1]/div[2]/div[1]/form/input[1]'
    Nietze_checkbox = '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/div/section/ul/li[4]/div/div[2]/div[3]/ul/li[1]/label/div'
    izdatel_azbuka_checkbox = '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/div/section/ul/li[6]/div/div[2]/div[3]/ul/li[3]/label/div'
    add_button = '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[1]'
    parsed_name_in_catalog_locator_Nietze = '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/h1'
    book_Nietze_locator = '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/section/section/div/article[2]/a[1]/picture/img'
    parsed_avtor_in_catalog_locator_Nietze = '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/a'
    parsed_izdatel_in_catalog_locator_Nietze = '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/a'
    ezoteric_filter_locator = '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/div/section/ul/li[2]/div/div[2]/ul/li/ul/li[3]/div/span[1]'
    izdatel_sofia_checkbox = '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/div/section/ul/li[6]/div/div[2]/div[3]/ul/li[4]/label/div'
    bookmark_button_locator = '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[3]/div/div[1]/div[1]/div[2]/div/div[2]'
    book_Gurjiev_locator = '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/section/section/div/article[1]/a[1]'
    parsed_name_in_catalog_locator_Gurjiev = '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/h1'
    parsed_avtor_in_catalog_locator_Gurjiev = '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div/div/a'
    parsed_izdatel_in_catalog_locator_Gurjiev = '//*[@id="__layout"]/div/div[3]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/a'



    """Getters"""

    def get_search_field(self):
        return self.driver.find_element(By.XPATH, self.search_field)

    def get_Nietze_checkbox(self):
        x = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, self.Nietze_checkbox)))
        return self.driver.find_element(By.XPATH, self.Nietze_checkbox)

    def get_izdatel_azbuka_checkbox(self):
        return self.driver.find_element(By.XPATH, self.izdatel_azbuka_checkbox)

    def get_izdatel_sofia_checkbox(self):
        return self.driver.find_element(By.XPATH, self.izdatel_sofia_checkbox)

    def get_parsed_name_in_catalog_Nietze(self):
        return self.driver.find_element(By.XPATH, self.parsed_name_in_catalog_locator_Nietze)

    def get_parsed_avtor_in_catalog_Nietze(self):
        return self.driver.find_element(By.XPATH, self.parsed_avtor_in_catalog_locator_Nietze)

    def get_parsed_izdatel_in_catalog_Nietze(self):
        return self.driver.find_element(By.XPATH, self.parsed_izdatel_in_catalog_locator_Nietze)

    def get_add_button(self):
        return self.driver.find_element(By.XPATH, self.add_button)

    def get_Nietze_book(self):
        return self.driver.find_element(By.XPATH, self.book_Nietze_locator)

    def get_ezoteric_filter(self):
        return self.driver.find_element(By.XPATH, self.ezoteric_filter_locator)

    def get_bookmark_button(self):
        return self.driver.find_element(By.XPATH, self.bookmark_button_locator)

    def get_book_Gurjiev(self):
        return self.driver.find_element(By.XPATH, self.book_Gurjiev_locator)

    def get_parsed_name_in_catalog_Gurjiev(self):
        return self.driver.find_element(By.XPATH, self.parsed_name_in_catalog_locator_Gurjiev)

    def get_parsed_avtor_in_catalog_Gurjiev(self):
        return self.driver.find_element(By.XPATH, self.parsed_avtor_in_catalog_locator_Gurjiev)

    def get_parsed_izdatel_in_catalog_Gurjiev(self):
        return self.driver.find_element(By.XPATH, self.parsed_izdatel_in_catalog_locator_Gurjiev)



    """Actions"""

# Нажимает на поле ввода
    def click_search_field(self):
        self.get_search_field().click()
        print("Search field Clicked")


# Вводит имя книги
    def input_name_of_product(self, name_of_product):
        self.get_search_field().send_keys(name_of_product)
        self.get_search_field().send_keys(Keys.RETURN)
        print("Name of product added in search field")


# Выбирает фильтр автора Ницше
    def add_Nietze_checkbox(self):
        self.driver.execute_script("window.scrollTo(0, 700)")
        time.sleep(1)
        self.get_Nietze_checkbox().click()
        print("Clicked on Nietze checkbox")


# Выбирает фильтр издателя Азбука
    def add_izdatel_azbuka_checkbox(self):
        self.driver.execute_script("window.scrollTo(0, 1500)")
        time.sleep(1)
        self.get_izdatel_azbuka_checkbox().click()
        print("Clicked on izdatel checkbox")


# Открывает книгу
    def click_on_Nietze_book(self):
        self.driver.execute_script("window.scrollTo(0, 100)")
        time.sleep(1)
        self.get_Nietze_book().click()
        print("Clicked on book")


# Парсит название книги
    def check_catalog_name_Nietze(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.parsed_name_in_catalog_locator_Nietze)))
        x = self.get_parsed_name_in_catalog_Nietze().text
        assert x == "Так говорил Заратустра"
        print("Name of product in catalog : " + x)
        return x


# Парсит имя автора
    def check_avtor_name_in_catalog_Nietze(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.parsed_avtor_in_catalog_locator_Nietze)))
        x = self.get_parsed_avtor_in_catalog_Nietze().text
        assert x == "Фридрих Ницше"
        print("Author's name in catalog : " + x)
        return x


# Парсит название издателя
    def check_izdatel_in_catalog_Nietze(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.parsed_izdatel_in_catalog_locator_Nietze)))
        x = self.get_parsed_izdatel_in_catalog_Nietze().text
        assert x == "Азбука"
        print("Izdatel is : " + x)


# Добавляет книгу в корзину
    def click_add_button(self):
        self.driver.execute_script("window.scrollTo(0, 100)")
        time.sleep(1)
        self.get_add_button().click()
        print("Clicked on add button")


# Выбирает фильтр Эзотерика
    def add_ezoteric_filter(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.ezoteric_filter_locator)))
        x = self.get_ezoteric_filter()
        x.click()
        print("Clicked on ezoteric filter")


# Выбирает фильтр издателя София
    def add_izdatel_sofia_checkbox(self):
        self.driver.execute_script("window.scrollTo(0, 1300)")
        time.sleep(1)
        self.get_izdatel_sofia_checkbox().click()
        print("Clicked on izdatel checkbox")


# Выбирает книгу
    def click_on_Gurjiev_book(self):
        self.get_book_Gurjiev().click()
        print("Clicked on book")


# Парсит название книги
    def check_catalog_name_Gurjiev(self):
        x = self.get_parsed_name_in_catalog_Gurjiev().text
        assert x == "В поисках Бытия: Четвертый Путь к Сознанию"
        print("Name of product in catalog : " + x)
        return x


# Парсит имя автора
    def check_avtor_name_in_catalog_Gurjiev(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.parsed_avtor_in_catalog_locator_Gurjiev)))
        x = self.get_parsed_avtor_in_catalog_Gurjiev().text
        assert x == "Георгий Гурджиев"
        print("Author's name in catalog : " + x)
        return x


# Парсит название издателя
    def check_izdatel_in_catalog_Gurjiev(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.parsed_izdatel_in_catalog_locator_Gurjiev)))
        x = self.get_parsed_izdatel_in_catalog_Gurjiev().text
        assert x == "София"
        print("Izdatel is : " + x)


# Добавляет книгу в закладки
    def add_book_in_bookmark(self):
        time.sleep(1)
        # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.bookmark_button_locator)))
        self.get_bookmark_button().click()
        print("Added book in bookmark")



    """All page action"""

# Проделывает основные шаги главной страницы по тесту test_buy_zaratustra
    def choose_zaratustra_book(self):
        spisok = [""]
        self.get_search_field()
        self.input_name_of_product('Заратустра')
        time.sleep(2)
        self.add_Nietze_checkbox()
        time.sleep(1)
        self.add_izdatel_azbuka_checkbox()
        self.click_on_Nietze_book()
        z = self.check_catalog_name_Nietze()
        spisok.append(z)
        y = self.check_avtor_name_in_catalog_Nietze()
        self.check_izdatel_in_catalog_Nietze()
        spisok.append(y)
        time.sleep(1)
        self.click_add_button()
        return spisok


# Проделывает основные шаги по тесту test_add_Gurjiev_on_bookmarks
    def choose_4th_way_book(self):
        self.get_search_field()
        self.input_name_of_product("Гурджиев")
        self.add_ezoteric_filter()
        time.sleep(1)
        self.add_izdatel_sofia_checkbox()
        time.sleep(1)
        self.click_on_Gurjiev_book()
        time.sleep(2)
        self.check_catalog_name_Gurjiev()
        self.check_avtor_name_in_catalog_Gurjiev()
        self.check_izdatel_in_catalog_Gurjiev()
        self.add_book_in_bookmark()




