from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class ShoppingCart:
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def shopping_cart_location(self):
        return self.driver.find_element(By.CSS_SELECTOR,".sp>h3")

    def shopping_cart_location_text(self):
        return self.shopping_cart_location().text[:13]

    def total_price(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"[colspan='2']>span")[3]

    def edit_button(self):
        return self.driver.find_elements(By.XPATH,"//*[text()='EDIT']")

    def want_to_edit(self,index):
        self.edit_button()[index].click()

    def quantity_of_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"[class='smollCell quantityMobile']>[class='ng-binding']")

    def check_quantity_of_specific_product(self,index):
        return self.quantity_of_product()[index]

    #add price of products