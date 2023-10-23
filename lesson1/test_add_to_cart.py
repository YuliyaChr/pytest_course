import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_add_to_cart(driver, fixture_login):

    pick_product = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link > div')
    pick_product.click()

    add_to_cart = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    add_to_cart.click()

    time.sleep(2)

    check_the_cart = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')
    check_the_cart.click()
    assert driver.current_url == "https://www.saucedemo.com/cart.html"

    driver.quit()

    # //div[contains(text(), 'Sauce Labs Backpack')]