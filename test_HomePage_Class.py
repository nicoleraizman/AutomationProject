from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Category_Page import Category_Page
from HomePage_Class import HomePage
from Product_Page import Product_Page
from Navigation_Class import Navigation
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class testAOS(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\selenium1\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service_chrome)

        self.driver.get("https://www.advantageonlineshopping.com/#/")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.Home_Page = HomePage(self.driver)
        self.Category_Page = Category_Page(self.driver)
        self.Product_Page = Product_Page(self.driver)
        self.Navigation_Bar = Navigation(self.driver)
        self.wait = WebDriverWait(self.driver,10)

    def testCase1(self):
        self.Home_Page.category_click(0)

        element = self.driver.find_element(By.CSS_SELECTOR, "[class='productName ng-binding']")
        self.driver.execute_script("arguments[0].click();", element)

        #product = self.driver.find_elements(By.CSS_SELECTOR, "[class='productName ng-binding']")
        #self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class='productName ng-binding']")))

        #self.Category_Page.pick_a_product(0)

        # element= self.driver.find_element(By.CSS_SELECTOR)
        # ActionChains(self.driver).move_to_element().send_keys(Keys.ARROW_DOWN).perform()

        self.Product_Page.change_quantity("3")
        self.Product_Page.click_add_to_cart()


        self.Navigation_Bar.click_homepage_button()


        self.Home_Page.category_click(1)
        self.Category_Page.pick_a_product(1)
        self.Product_Page.change_quantity("2")
        self.Product_Page.click_add_to_cart()








