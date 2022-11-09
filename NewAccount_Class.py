from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class NewAccount:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def username_field(self, username:str):
        self.driver.find_element(By.CSS_SELECTOR, "usernameRegisterPage").send_keys(username)

    def email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, "emailRegisterPage").send_keys(email)

    def password_field(self, password):
        self.driver.find_element(By.CSS_SELECTOR, "input[class = 'ng-pristine ng-valid ng-scope ng-touched invalid'][name = 'passwordRegisterPage']").send_keys(password)

    def confirm_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, "confirm_passwordRegisterPage").send_keys(password)

    def i_agree_checkbox(self):
        return self.driver.find_element(By.NAME, "i_agree")

    def i_agree_checkbox_click(self):
        self.i_agree_checkbox().click()

    def register_button(self):
        return self.driver.find_element(By.ID, "register_btnundefined")

    def click_register_button(self):
       self.register_button().click()