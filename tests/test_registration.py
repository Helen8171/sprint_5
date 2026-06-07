from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, AuthLocators, RegLocators
from data import Constants

class TestRegistration:
    def test_successful_registration(self, driver, random_email):
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_REG_BTN)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)).click()
        
        wait.until(EC.visibility_of_element_located(RegLocators.CREATE_ACCOUNT_BTN))
        
        wait.until(EC.visibility_of_element_located(RegLocators.EMAIL_INPUT)).send_keys(random_email)
        wait.until(EC.visibility_of_element_located(RegLocators.PASSWORD_INPUT)).send_keys(Constants.VALID_PASSWORD)
        wait.until(EC.visibility_of_element_located(RegLocators.REPEAT_PASSWORD_INPUT)).send_keys(Constants.VALID_PASSWORD)
        wait.until(EC.element_to_be_clickable(RegLocators.CREATE_ACCOUNT_BTN)).click()
        
        avatar_displayed = wait.until(EC.visibility_of_element_located(HeaderLocators.USER_AVATAR)).is_displayed()
        assert avatar_displayed is True

    def test_registration_invalid_email(self, driver, invalid_email):
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_REG_BTN)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)).click()
        
        wait.until(EC.visibility_of_element_located(RegLocators.CREATE_ACCOUNT_BTN))
        
        wait.until(EC.visibility_of_element_located(RegLocators.EMAIL_INPUT)).send_keys(invalid_email)
        wait.until(EC.element_to_be_clickable(RegLocators.CREATE_ACCOUNT_BTN)).click()
        
        error_displayed = wait.until(EC.visibility_of_element_located(RegLocators.EMAIL_ERROR_MSG)).is_displayed()
        assert error_displayed is True

    def test_registration_existing_user(self, driver, existing_user_data):
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_REG_BTN)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)).click()
        
        wait.until(EC.visibility_of_element_located(RegLocators.CREATE_ACCOUNT_BTN))
        
        wait.until(EC.visibility_of_element_located(RegLocators.EMAIL_INPUT)).send_keys(existing_user_data["email"])
        wait.until(EC.visibility_of_element_located(RegLocators.PASSWORD_INPUT)).send_keys(existing_user_data["password"])
        wait.until(EC.visibility_of_element_located(RegLocators.REPEAT_PASSWORD_INPUT)).send_keys(existing_user_data["password"])
        wait.until(EC.element_to_be_clickable(RegLocators.CREATE_ACCOUNT_BTN)).click()
        
        error_displayed = wait.until(EC.visibility_of_element_located(RegLocators.EMAIL_ERROR_MSG)).is_displayed()
        assert error_displayed is True