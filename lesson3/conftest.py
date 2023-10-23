import pytest
from selenium import webdriver
from locators import START_BUTTON, LOGIN_FIELD, PASSWORD_FIELD
from data import LOGIN, PASSWORD, MAIN_PAGE
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()