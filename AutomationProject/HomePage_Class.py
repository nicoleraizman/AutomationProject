from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def category_element(self):
        return self.driver.find_elements(By.CLASS_NAME, "categoryCell")

    def category_click(self, index):
        self.category_element()[index].click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select  ng-binding")))

    def user_icon(self):
        return self.driver.find_element(By.ID, "menuUser")

    def user_icon_click(self):
        self.driver.find_element(By.ID, "menuUser").click()

    def username_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name = 'username']")

    def enter_username(self, username):
        self.username_element().send_keys(username)

    def password_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[name = 'password']")

    def enter_password(self, password):
        self.password_element().send_keys(password)

    def sign_in_button(self):
        return self.driver.find_element(By.ID, "sign_in_btnundefined")

    def sign_in_button_click(self):
       self.sign_in_button().click()

       # self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "hi-user containMiniTitle ng-binding")))
       # self.wait.until(EC.element_to_be_clickable((By.ID, "menuUser")))

# two of the functions do not work, ask Alon
    def sign_out_button(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "menuUser")))
        self.driver.find_element(By.ID, "menuUserSVGPath").click()
        dropdown_list = self.driver.find_elements(By.ID, "loginMiniTitle")
        return dropdown_list[2]


    def sign_out_button_click(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "menuUser")))
        element = self.driver.find_element(By.ID, "menuUser")
        self.driver.execute_script("arguments[0].click();", element)
        self.sign_out_button().click()


    # def sign_out_button(self):
    #     self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "hi-user containMiniTitle ng-binding")))
    #     return self.driver.find_element(By.CSS_SELECTOR, "signOut($event)")
    #
    # def click_sign_out_button(self):
    #     self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "hi-user containMiniTitle ng-binding")))
    #     self.sign_out_button().click()

    def cart_menu(self):
        return self.driver.find_element(By.ID, "menuCart")

    def cart_menu_click(self):
        self.driver.find_element(By.ID, "menuCart").click()



