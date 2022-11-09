from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Product_Page:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def product_name(self):
        return self.driver.find_element(By.CSS_SELECTOR,"#Description>h1")

    def product_name_text(self):
        return self.product_name().text

    def product_price(self):
        return self.driver.find_element(By.CSS_SELECTOR,"#Description>h2")

    def colors_list(self):
        return self.driver.find_elements(By.ID,"rabbit")


    def choose_color(self,color):
        return self.driver.find_elements(By.CSS_SELECTOR,f"[title='{color}']")


    def pick_color(self,index):
        self.colors_list()[index].click()

    def quantity_of_product(self):
        return self.driver.find_element(By.NAME,"quantity")

    def change_quantity(self,num:str):
        self.quantity_of_product().click()
        ActionChains(self.driver).move_to_element(self.quantity_of_product()).send_keys(Keys.DELETE).perform()
        self.quantity_of_product().send_keys(num)
        return num

    def add_to_cart_button(self):
        return self.driver.find_element(By.XPATH,"//div/button")


    def click_add_to_cart(self):
        self.add_to_cart_button().click()


