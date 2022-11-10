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

<<<<<<< HEAD
    def cart_icon_hover(self):
=======
    def cart_icon(self):
>>>>>>> 10f7509676f1a942933dd990eb6027a5a8982aba
        element = self.driver.find_element(By.ID, "menuCart")
        ActionChains(self.driver).move_to_element(element).perform()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[class = 'roboto-regular ng-binding']")))

<<<<<<< HEAD
    def cart_icon(self):
        return self.driver.find_element(By.ID, "menuCart")

    def click_cart_icon(self):
        self.cart_icon().click()

=======
>>>>>>> 10f7509676f1a942933dd990eb6027a5a8982aba
    def total_sum_in_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[class = 'roboto-regular ng-binding']")

    def total_sum_text(self):
        return self.total_sum_in_cart().text

    def quantity_of_product_in_cart(self, index):
        product_list = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td>a>label")
<<<<<<< HEAD
        return product_list[index*2].text[5:]

    def change_to_int_quantity_of_product(self,index):
        return int(self.quantity_of_product_in_cart(index))

=======
        for index in range(len(product_list)):
            if index%2 == 0:
                return product_list[index].text
            else:
                pass
>>>>>>> 10f7509676f1a942933dd990eb6027a5a8982aba


    #make sure slicing is correct
    def colors_of_products_in_cart(self, index):
        product_list = self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td>a>label>span")
<<<<<<< HEAD
        return product_list[index].text

=======
        for index in range(len(product_list)):
            if index%2 != 0:
                return product_list[index].text[7:]
            else:
                pass
>>>>>>> 10f7509676f1a942933dd990eb6027a5a8982aba


    def name_of_products_in_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td>a>h3")
        #return product_list[index]

    def name_of_products_in_cart_text(self,index):
        return self.name_of_products_in_cart()[index].text[0:27]

<<<<<<< HEAD
    def price_of_each_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"tbody>tr>td>p")

    def price_of_each_product_text(self,index):
        return self.price_of_each_product()[index].text[1:]

    def price_of_each_product_to_float(self,index):
        return float(self.price_of_each_product_text(index))


    def remove_item_from_the_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td>div>div")

    def click_on_remove_item_from_the_cart(self, index):
        self.remove_item_from_the_cart()[index].click()


=======
>>>>>>> 10f7509676f1a942933dd990eb6027a5a8982aba









