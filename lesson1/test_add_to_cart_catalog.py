from selenium import webdriver
from selenium.webdriver.common.by import By


def test_add_to_cart_catalog(driver, fixture_login):

    text_before = driver.find_element(By.ID, 'item_4_title_link').text

    button = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    button.click()

    cart = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart.click()

    text_after = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]').text
    assert text_before == text_after
