import pytest
from selenium import webdriver
from data import Urls

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()