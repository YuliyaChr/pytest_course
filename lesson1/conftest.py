import pytest
from selenium import webdriver
from locators import LOGIN_BUTTON, USERNAME_FIELD, PASSWORD_FIELD
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

# @pytest.fixture
# def test_fixture_login(driver):
#     driver.get(MAIN_PAGE)
#
#     username_field = driver.find_element(By.ID, USERNAME_FIELD)
#     username_field.send_keys(LOGIN)
#
#     password_field = driver.find_element(By.ID, PASSWORD_FIELD)
#     password_field.send_keys(PASSWORD)
#
#     main_page = driver.find_element(By.ID, LOGIN_BUTTON).click()
#     yield main_page