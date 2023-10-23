import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from locators import LOGIN_BUTTON, USERNAME_FIELD, PASSWORD_FIELD
from data import LOGIN, PASSWORD, MAIN_PAGE


driver = webdriver.Chrome()
driver.maximize_window()

@pytest.fixture
def test_fixture_login():
    driver.get(MAIN_PAGE)

    username_field = driver.find_element(By.ID, USERNAME_FIELD)
    username_field.send_keys(LOGIN)

    password_field = driver.find_element(By.ID, PASSWORD_FIELD)
    password_field.send_keys(PASSWORD)

    main_page = driver.find_element(By.ID, LOGIN_BUTTON).click()
    yield main_page


def test_logout(test_fixture_login):
    url_before = MAIN_PAGE

    burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(2)

    logout = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    logout.click()

    url_after = driver.current_url

    assert url_before == url_after
