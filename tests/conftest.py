import pytest
import random
import string
from selenium import webdriver
from data import Constants

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(Constants.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def random_email():
    domain = random.choice(["mail.ru", "gmail.com", "yandex.ru"])
    prefix = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{prefix}@{domain}"

@pytest.fixture(scope="function")
def invalid_email():
    return "invalid_email_format"

@pytest.fixture(scope="function")
def existing_user_data():
    return {
        "email": "zanyato@mail.ru",
        "password": "Password123!"
    }