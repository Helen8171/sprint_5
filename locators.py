from selenium.webdriver.common.by import By

class HeaderLocators:
    LOGIN_REG_BTN = (By.XPATH, "//button[contains(., 'Вход и регистрация')]")
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    LOGOUT_BTN = (By.XPATH, "//button[contains(., 'Выйти')]")
    CREATE_AD_BTN = (By.XPATH, "//button[contains(., 'Разместить объявление')]")

class AuthLocators:
    NO_ACCOUNT_BTN = (By.XPATH, "//button[contains(., 'Нет аккаунта')]")
    LOGIN_EMAIL_INPUT = (By.XPATH, "(//input[@name='email'])[1]")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "(//input[@name='password'])[1]")
    LOGIN_BTN = (By.XPATH, "//button[contains(., 'Войти')]")

class RegLocators:
    EMAIL_INPUT = (By.XPATH, "(//input[@name='email'])[last()]")
    PASSWORD_INPUT = (By.XPATH, "(//input[@type='password'])[last()-1]")
    REPEAT_PASSWORD_INPUT = (By.XPATH, "(//input[@type='password'])[last()]")
    CREATE_ACCOUNT_BTN = (By.XPATH, "//button[contains(., 'Создать аккаунт')]")
    EMAIL_ERROR_MSG = (By.XPATH, "//span[text()='Ошибка']")

class AdLocators:
    AUTH_MODAL_TITLE = (By.XPATH, "//h1[contains(., 'Чтобы разместить объявление, авторизуйтесь')]")
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    CONDITION_NEW_RADIO = (By.XPATH, "//label[text()='Новый']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price']")
    PUBLISH_BTN = (By.XPATH, "//button[contains(., 'Опубликовать')]")