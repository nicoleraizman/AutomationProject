from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class LogoSection:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def cart_icon(self):
        element = self.driver.find_element(By.ID, "menuCart")
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[class = 'roboto-regular ng-binding']")))

    def total_sum_in_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[class = 'roboto-regular ng-binding']")

    def total_sum_text(self):
        return self.total_sum_in_cart().text

    def quantity_of_product_in_cart(self, index):
        product_list = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td>a>label")
        for index in range(len(product_list)):
            if index%2 == 0:
                return product_list[index].text
            else:
                pass


    #make sure slicing is correct
    def colors_of_products_in_cart(self, index):
        product_list = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td>a>label>span")
        for index in range(len(product_list)):
            if index%2 != 0:
                return product_list[index].text[7:]
            else:
                pass


    def name_of_products_in_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td>a>h3")
        #return product_list[index]

    def name_of_products_in_cart_text(self,index):
        return self.name_of_products_in_cart()[index].text[0:27]










