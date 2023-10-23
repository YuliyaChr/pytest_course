from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_remove_from_cart(driver, fixture_login):

    pick_product = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link > div')
    pick_product.click()

    add_to_cart = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    add_to_cart.click()

    time.sleep(2)

    check_the_cart_before = driver.find_element(By.CSS_SELECTOR, 'span.shopping_cart_badge')
    assert check_the_cart_before.text == '1'

    go_to_cart = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')
    go_to_cart.click()
    time.sleep(2)

    remove_from_cart = driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
    remove_from_cart.click()
    time.sleep(2)

    check_the_cart_after = driver.find_element(By.CSS_SELECTOR, '.removed_cart_item')
    assert check_the_cart_after.text == ''

    driver.quit()

