import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from data import LOGIN, PASSWORD, MAIN_PAGE


def test_logout(driver, fixture_login):
    url_before = MAIN_PAGE

    burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(2)

    logout = driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link')
    logout.click()

    url_after = driver.current_url

    assert url_before == url_after
