import pytest
from selenium import webdriver
from base.base_class import Base

@pytest.fixture()
def set_up():
    print("\nTest started")
    yield
    print("Test finished")