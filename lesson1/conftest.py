import pytest
from selenium import webdriver
from locators import LOGIN_BUTTON, USERNAME_FIELD, PASSWORD_FIELD
from data import LOGIN, PASSWORD, MAIN_PAGE
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()

@pytest.fixture()
def fixture_login(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.ID, USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.ID, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.ID, LOGIN_BUTTON).click()