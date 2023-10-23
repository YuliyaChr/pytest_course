import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import START_BUTTON, LOGIN_FIELD, PASSWORD_FIELD, REGISTER_BUTTON, CHECKBOX, SUCCESS_MESSAGE, LOADER
from data import LOGIN, PASSWORD, MAIN_PAGE


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()


def test_registration(driver):
    driver.get(MAIN_PAGE)
    header = driver.find_element(By.XPATH, '//h1')
    assert header.text == "Практика с ожиданиями в Selenium"

    time.sleep(5)

    start_button = driver.find_element(By.ID, START_BUTTON)
    start_button.click()

    login_field = driver.find_element(By.ID, LOGIN_FIELD)
    login_field.send_keys(LOGIN)

    password_field = driver.find_element(By.ID, PASSWORD_FIELD)
    password_field.send_keys(PASSWORD)

    checkbox_field = driver.find_element(By.ID, CHECKBOX)
    checkbox_field.click()


    register_button = driver.find_element(By.ID, REGISTER_BUTTON)
    register_button.click()

    time.sleep(1)

    loader_button = driver.find_element(By.ID, LOADER)
    print(loader_button.is_displayed())

    time.sleep(4)

    success_message = driver.find_element(By.ID, SUCCESS_MESSAGE)
    assert success_message.text == "Вы успешно зарегистрированы!"




