from selenium.webdriver.common.by import By


class LoginPage():

    # Locators
    USERNAME_INPUT = "Username"
    PASSWORD_INPUT = "Password"
    BUTTON_LOGIN = "submit"
    OPTION_USER = "oxd-userdropdown-icon"

    # Methods
    def __init__(self, driver):
        self.driver = driver

    # Acciones
    def login_in_app(self, username, password):
        username_input = self.driver.find_element(By.XPATH, f"//input[@placeholder='{self.USERNAME_INPUT}']")
        username_input.send_keys(username)

        password_input = self.driver.find_element(By.XPATH, f"//input[@placeholder='{self.PASSWORD_INPUT}']")
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.XPATH, f"//button[@type='{self.BUTTON_LOGIN}']")
        login_button.click()

    def is_login_successful(self):
        user_option = self.driver.find_element(By.CLASS_NAME, f"{self.OPTION_USER}").is_displayed()
        return user_option
