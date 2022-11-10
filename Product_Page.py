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
        self.list_colors = []


    def product_name(self):
        return self.driver.find_element(By.CSS_SELECTOR,"#Description>h1")

    def product_name_text(self):
        return self.product_name().text

    def product_price(self):
        return self.driver.find_element(By.CSS_SELECTOR,"#Description>h2")

    def product_price_text(self):
        return self.product_price().text[1:]

    def product_price_text_to_float(self):
        return float(self.product_price_text())

    def colors_list(self):
        self.list_colors = self.driver.find_elements(By.ID,"rabbit")

    def colors_list_text(self,index):
        return self.list_colors[index].get_attribute("title")

    def click_on_color(self,index):
        element = self.list_colors[index]
        self.driver.execute_script("arguments[0].click();", element)







    # def choose_color(self,color):
    #     return self.driver.find_element(By.CSS_SELECTOR,f"[title='{color}']")

    # def choose_color_text(self, color):
    #     return self.choose_color(color).text


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


