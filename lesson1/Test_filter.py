FILTER = (By.XPATH, "//select[contains(@class, 'product_sort')]")
LOW_HIGH = (By.XPATH, "//span[@class='active_option']")
PRICES = (By.XPATH, "//div[@class='inventory_item_price']")
ITEM_NAMES = (By.XPATH, "//div[@class='inventory_item_name ']")
def test_filter_a_to_z(login):
    Select(login.find_element(*FILTER)).select_by_index(0)
    items = login.find_elements(*ITEM_NAMES)
    list_items = [item.text.split() for item in items]
    items_order = [[ord(x[0]) for x in l] for l in list_items]
    previous = items_order[0]
    for item in items_order:
        ind = 0
        while len(item) < len(previous):
            item.append(0)
        while len(previous) < len(item):
            previous.append(0)
        for num in previous:
            if item[ind] < num and item[ind - 1] < previous[ind - 1]:
                assert 1 > 2, f"Not filtered properly {num}, {item[ind]} - {item[ind - 1]}"
            ind += 1
        previous = item






        this is my
        fixture
        which is located
        on
        coftest.py:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        BASE_URL = "https://www.saucedemo.com/"
        STANDARD_USER = "standard_user"
        STANDARD_PASS = "secret_sauce"
        USER_NAME = (By.XPATH, "//form // input[@placeholder='Username']")
        USER_PASS = (By.XPATH, "//input[contains(@type, 'passw')]")
        LOGIN = (By.XPATH, "//input[@data-test='login-button']")
        NEEDED_URL = 'inventory'
        LOGO_TEXT = "Swag Labs"
        LOGO_TEXT_ACTUAL = (By.XPATH, "//div[@class='app_logo' and text()='Swag Labs']")

        @pytest.fixture(scope='session')
        def driver():
            print('\nstart browser...')
            chrome_options = Options()
            if 'CI' in os.environ:
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-dev-shm-usage')
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
                driver.maximize_window()
            else:
                driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
                driver.maximize_window()
            yield driver
            print('\nquit browser...')
            driver.quit()

        @pytest.fixture(scope='session')
        def login(driver):
            driver.get(BASE_URL)
            driver.find_element(*USER_NAME).send_keys(STANDARD_USER)
            driver.find_element(*USER_PASS).send_keys(STANDARD_PASS)
            driver.find_element(*LOGIN).click()
            assert NEEDED_URL in driver.current_url, f"{NEEDED_URL} is missing from the url"
            text = driver.find_element(*LOGO_TEXT_ACTUAL).text
            assert LOGO_TEXT == text, f"Expected text: {LOGO_TEXT} is not equal to actual: {LOGO_TEXT_ACTUAL}"
            yield driver

        _____________
        and these
        are
        my
        test
        for filter test cases:
            from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.support.ui import WebDriverWait, Select
        from selenium.webdriver.support import expected_conditions as EC
        FILTER = (By.XPATH, "//select[contains(@class, 'product_sort')]")
        LOW_HIGH = (By.XPATH, "//span[@class='active_option']")
        PRICES = (By.XPATH, "//div[@class='inventory_item_price']")
        ITEM_NAMES = (By.XPATH, "//div[@class='inventory_item_name ']")

        # Проверка работоспособности фильтра (low to high)
        def test_filter_low_to_high(login):
            Select(login.find_element(*FILTER)).select_by_index(2)
            prices = login.find_elements(*PRICES)
            assert len(prices) == 6
            n = float(prices[0].text[1:])
            for num in prices:
                assert n <= float(num.text[1:]), f"Not filtered properly"
                n = float(num.text[1:])

        # Проверка работоспособности фильтра (high to low)
        def test_filter_high_to_low(login):
            Select(login.find_element(*FILTER)).select_by_index(3)
            prices = login.find_elements(*PRICES)
            assert len(prices) == 6
            n = float(prices[0].text[1:])
            for num in prices:
                assert n >= float(num.text[1:]), f"Not filtered properly"
                n = float(num.text[1:])

        # Проверка работоспособности фильтра (A to Z)
        def test_filter_a_to_z(login):
            Select(login.find_element(*FILTER)).select_by_index(0)
            items = login.find_elements(*ITEM_NAMES)
            list_items = [item.text.split() for item in items]
            items_order = [[ord(x[0]) for x in l] for l in list_items]
            previous = items_order[0]
            for item in items_order:
                ind = 0
                while len(item) < len(previous):
                    item.append(0)
                while len(previous) < len(item):
                    previous.append(0)
                for num in previous:
                    if item[ind] < num and item[ind - 1] < previous[ind - 1]:
                        assert 1 > 2, f"Not filtered properly {num}, {item[ind]} - {item[ind - 1]}"
                    ind += 1
                previous = item

        # Проверка работоспособности фильтра (Z to A)
        def test_filter_z_to_a(login):
            Select(login.find_element(*FILTER)).select_by_index(1)
            items = login.find_elements(*ITEM_NAMES)
            list_items = [item.text.split() for item in items]
            items_order = [[ord(x[0]) for x in l] for l in list_items]
            previous = items_order[0]
            for item in items_order:
                ind = 0
                while len(item) < len(previous):
                    item.append(0)
                while len(previous) < len(item):
                    previous.append(0)
                for num in previous:
                    if item[ind] > num and item[ind - 1] > previous[ind - 1]:
                        assert 1 > 2, f"Not filtered properly {num}, {item[ind]} - {item[ind - 1]}"
                    ind += 1
                previous = item