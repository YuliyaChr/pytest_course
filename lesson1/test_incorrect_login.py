from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_incorrect_login():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("user")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(2)

    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container.error").text
    time.sleep(2)
    assert error_message == 'Epic sadface: Username and password do not match any user in this service'

    driver.quit()
