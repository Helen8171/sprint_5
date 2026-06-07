from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, AuthLocators

class TestLogin:
    def test_successful_login(self, driver, existing_user_data):
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_REG_BTN)).click()
        
        wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_EMAIL_INPUT)).send_keys(existing_user_data["email"])
        driver.find_element(*AuthLocators.LOGIN_PASSWORD_INPUT).send_keys(existing_user_data["password"])
        driver.find_element(*AuthLocators.LOGIN_BTN).click()
        
        avatar_displayed = wait.until(EC.visibility_of_element_located(HeaderLocators.USER_AVATAR)).is_displayed()
        assert avatar_displayed is True