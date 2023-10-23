from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_about_button(driver, fixture_login):

    burger_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    burger_menu.click()
    time.sleep(2)

    about_button = driver.find_element(By.CSS_SELECTOR, '#about_sidebar_link')
    about_button.click()

    time.sleep(2)

    assert driver.current_url == "https://saucelabs.com/"

