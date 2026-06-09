from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, AuthLocators, RegLocators
from data import TestData, Credentials
from helpers import generate_random_email

class TestRegistration:
    def test_successful_registration(self, driver):
        wait = WebDriverWait(driver, 10)
        random_email = generate_random_email()
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_REG_BTN)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)).click()
        wait.until(EC.visibility_of_element_located(RegLocators.CREATE_ACCOUNT_BTN))
        
        wait.until(EC.visibility_of_element_located(RegLocators.EMAIL_INPUT)).send_keys(random_email)
        wait.until(EC.visibility_of_element_located(RegLocators.PASSWORD_INPUT)).send_keys(TestData.VALID_PASSWORD)
        wait.until(EC.visibility_of_element_located(RegLocators.REPEAT_PASSWORD_INPUT)).send_keys(TestData.VALID_PASSWORD)
        wait.until(EC.element_to_be_clickable(RegLocators.CREATE_ACCOUNT_BTN)).click()
        
        assert wait.until(EC.visibility_of_element_located(HeaderLocators.USER_AVATAR)).is_displayed()

    def test_registration_invalid_email(self, driver):
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_REG_BTN)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)).click()
        wait.until(EC.visibility_of_element_located(RegLocators.CREATE_ACCOUNT_BTN))
        
        wait.until(EC.visibility_of_element_located(RegLocators.EMAIL_INPUT)).send_keys(TestData.INVALID_EMAIL)
        wait.until(EC.element_to_be_clickable(RegLocators.CREATE_ACCOUNT_BTN)).click()
        
        assert wait.until(EC.visibility_of_element_located(RegLocators.EMAIL_ERROR_MSG)).is_displayed()

    def test_registration_existing_user(self, driver):
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_REG_BTN)).click()
        wait.until(EC.element_to_be_clickable(AuthLocators.NO_ACCOUNT_BTN)).click()
        wait.until(EC.visibility_of_element_located(RegLocators.CREATE_ACCOUNT_BTN))
        
        wait.until(EC.visibility_of_element_located(RegLocators.EMAIL_INPUT)).send_keys(Credentials.EXISTING_USER_EMAIL)
        wait.until(EC.visibility_of_element_located(RegLocators.PASSWORD_INPUT)).send_keys(Credentials.EXISTING_USER_PASSWORD)
        wait.until(EC.visibility_of_element_located(RegLocators.REPEAT_PASSWORD_INPUT)).send_keys(Credentials.EXISTING_USER_PASSWORD)
        wait.until(EC.element_to_be_clickable(RegLocators.CREATE_ACCOUNT_BTN)).click()
        
        assert wait.until(EC.visibility_of_element_located(RegLocators.EMAIL_ERROR_MSG)).is_displayed()