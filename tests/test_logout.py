from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import HeaderLocators, AuthLocators

class TestLogout:
    def test_logout(self, driver, existing_user_data):
        wait = WebDriverWait(driver, 10)
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGIN_REG_BTN)).click()
        wait.until(EC.visibility_of_element_located(AuthLocators.LOGIN_EMAIL_INPUT)).send_keys(existing_user_data["email"])
        driver.find_element(*AuthLocators.LOGIN_PASSWORD_INPUT).send_keys(existing_user_data["password"])
        driver.find_element(*AuthLocators.LOGIN_BTN).click()
        
        wait.until(EC.element_to_be_clickable(HeaderLocators.LOGOUT_BTN)).click()
        
        login_btn_displayed = wait.until(EC.visibility_of_element_located(HeaderLocators.LOGIN_REG_BTN)).is_displayed()
        
        avatars = driver.find_elements(*HeaderLocators.USER_AVATAR)
        
        assert login_btn_displayed is True
        assert len(avatars) == 0