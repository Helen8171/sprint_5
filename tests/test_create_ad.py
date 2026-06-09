from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, AuthLocators, AdLocators
from data import Credentials

class TestCreateAd:
    def test_create_ad_unauthorized(self, driver):
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.CREATE_AD_BTN)).click()
        
        assert wait.until(EC.visibility_of_element_located(AdLocators.AUTH_MODAL_TITLE)).is_displayed()

    def test_create_ad_authorized(self, driver):
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_REG_BTN)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_EMAIL_INPUT)).send_keys(Credentials.EXISTING_USER_EMAIL)
        driver.find_element(*AuthLocators.LOGIN_PASSWORD_INPUT).send_keys(Credentials.EXISTING_USER_PASSWORD)
        driver.find_element(*AuthLocators.LOGIN_BTN).click()
        
        wait.until(EC.visibility_of_element_located(HeaderLocators.USER_AVATAR))
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.CREATE_AD_BTN)).click()
        
        wait.until(EC.visibility_of_element_located(AdLocators.NAME_INPUT)).send_keys("Мощный ноутбук")
        wait.until(EC.element_to_be_clickable(AdLocators.CONDITION_NEW_RADIO)).click()
        driver.find_element(*AdLocators.DESCRIPTION_INPUT).send_keys("Почти не использовался, идеальное состояние.")
        driver.find_element(*AdLocators.PRICE_INPUT).send_keys("85000")
        
        driver.find_element(*AdLocators.PUBLISH_BTN).click()
        
        assert wait.until(EC.invisibility_of_element_located(AdLocators.PUBLISH_BTN))