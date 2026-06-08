from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, AuthLocators
from data import Credentials

class TestLogin:
    def test_successful_login(self, driver):
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_REG_BTN)).click()
        
        wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_EMAIL_INPUT)).send_keys(Credentials.EXISTING_USER_EMAIL)
        driver.find_element(*AuthLocators.LOGIN_PASSWORD_INPUT).send_keys(Credentials.EXISTING_USER_PASSWORD)
        driver.find_element(*AuthLocators.LOGIN_BTN).click()
        
        assert wait.until(EC.visibility_of_element_located(HeaderLocators.USER_AVATAR)).is_displayed()