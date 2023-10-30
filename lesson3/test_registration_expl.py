import pytest
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from locators import START_BUTTON, LOGIN_FIELD, PASSWORD_FIELD, REGISTER_BUTTON, CHECKBOX, SUCCESS_MESSAGE, LOADER
from data import LOGIN, PASSWORD, MAIN_PAGE
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    return driver


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


def test_registration_explicit(driver, wait):
    driver.get(MAIN_PAGE)
    header = driver.find_element(By.XPATH, '//h1')
    assert header.text == "Практика с ожиданиями в Selenium"

    start_button = wait.until(EC.element_to_be_clickable((By.ID, START_BUTTON)))
    assert start_button.text == 'Начать тестирование'
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




