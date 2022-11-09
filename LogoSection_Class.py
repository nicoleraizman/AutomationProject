from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LogoSection:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def cart_icon(self):
        return self.driver.find_element(By.ID,"menuCart")

    def click_cart_icon(self):
        self.cart_icon().click()

    def product_in_cart_quantity(self, index):
        return self.driver.find_elements(By.CSS_SELECTOR, "tr>td>a>label[class = 'ng-binding']")[index]

    def total_quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[class = 'roboto-regular ng-binding']").text[1:" "]

    def color(self):
        table = self.driver.find_element(By.CLASS_NAME, "table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows[1:]:
            cols = row.find_elements(By.TAG_NAME, "td")
            for col in cols:
                print(col.text, end="\t")




