import time
import pytest
from base.base_class import Base
from selenium import webdriver
from pages.main_page import Main_page
from pages.cart_page import Cart_page


def test_buy_zaratustra(set_up):
    base_url = "https://www.chitai-gorod.ru/"
    driver = webdriver.Chrome()
    base = Base(driver)
    base.open_browser(base_url)
    base.get_current_url()
    main_page = Main_page(driver)
    time.sleep(3)
    main_page.get_search_field()
    main_page.input_name_of_product('Заратустра')
    time.sleep(3)
    main_page.add_Nietze_checkbox()
    time.sleep(3)
    main_page.add_izdatel_checkbox()
    time.sleep(3)
    z = main_page.check_catalog_name()
    time.sleep(3)
    main_page.click_add_button()
    time.sleep(3)
    cart_page = Cart_page(driver)
    cart_page.open_cart()
    time.sleep(3)
    y = cart_page.check_cart_name()
    if z == y:
        print("Names matched!")
    else:
        print("Wrong names")
    cart_page.click_oformlenie_button()
    time.sleep(3)
    base.get_screen()
    time.sleep(3)
    driver.quit()

    """ Thank You for attention :) """
