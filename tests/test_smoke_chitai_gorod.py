import time
import pytest
from base.base_class import Base
from selenium import webdriver
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from selenium.webdriver.common.by import By

# Ищет книгу Заратустра с фильтрами, добавляет в коризну, парсит данные и покупает книгу
def test_buy_zaratustra(set_up):
    base_url = "https://www.chitai-gorod.ru/"
    driver = webdriver.Chrome()
    base = Base(driver)
    base.open_browser(base_url)
    base.get_current_url()
    main_page = Main_page(driver)
    x = main_page.choose_zaratustra_book()
    cart_page = Cart_page(driver)
    y = cart_page.parsing_chosen_data()

    if x[1] == y[1]:
        print("Names matched!")
    else:
        print("Wrong names")
    if x[2] == y[2]:
        print("Authors matched!")
    else:
        print("Wrong authors")
    cart_page.click_oformlenie_button()
    time.sleep(1)
    cart_page.input_number("000000000")
    base.get_screen("test_buy_zaratustra")
    driver.quit()


# Ищет книгу Гурджиева с фильтрами, парсит данные выбранной книги и добавляет ее в закладки
def test_add_Gurjiev_on_bookmarks(set_up):
    base_url = "https://www.chitai-gorod.ru/"
    driver = webdriver.Chrome()
    base = Base(driver)
    base.open_browser(base_url)
    base.get_current_url()
    main_page = Main_page(driver)
    main_page.choose_4th_way_book()
    time.sleep(2)
    cart_page = Cart_page(driver)
    cart_page.input_number("000000000")
    base.get_screen("test_add_book_on_bookmarks")
    driver.quit()




""" Thank You for attention :) """
