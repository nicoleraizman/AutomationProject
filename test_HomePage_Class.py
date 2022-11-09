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
from LogoSection_Class import LogoSection
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class TestAOS(TestCase):
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
        self.Logo_Section = LogoSection(self.driver)

    def testCase1(self):
        self.Home_Page.category_click(0)
        self.Category_Page.pick_a_product(0)
        sleep(2)
        quantity1 = self.Product_Page.change_quantity("2")
        sleep(2)
        self.Product_Page.click_add_to_cart()
        sleep(2)
        self.Navigation_Bar.click_homepage_button()
        self.Home_Page.category_click(1)
        sleep(2)
        self.Category_Page.pick_a_product(1)
        sleep(2)
        quantity2 = self.Product_Page.change_quantity("9")
        sleep(2)
        self.Product_Page.click_add_to_cart()

        first = int(quantity1)
        second = int(quantity2)
        final_quantity = first + second
        print(final_quantity)
        self.Logo_Section.cart_icon()
        total = self.Logo_Section.total_sum_text()
        #(5 items)
        total = total[1:-7]
        total = int(total)
        print(total)
        self.assertEqual(total,final_quantity)


    def testcase2(self):
        self.Home_Page.category_click(0)
        self.Category_Page.pick_a_product(1)
        product1_name = self.Product_Page.product_name_text()
        print(product1_name)
        #sleep(2)
        quantity1 = self.Product_Page.change_quantity("2")
        #sleep(2)
        self.Product_Page.click_add_to_cart()
        #sleep(2)

        self.Navigation_Bar.click_homepage_button()
        self.Home_Page.category_click(1)
        #sleep(2)
        self.Category_Page.pick_a_product(1)
        product2_name = self.Product_Page.product_name_text()
        print(product2_name)
        #sleep(2)
        quantity2 = self.Product_Page.change_quantity("3")

        self.Product_Page.click_add_to_cart()

        self.Navigation_Bar.click_homepage_button()
        self.Home_Page.category_click(3)
        sleep(2)
        self.Category_Page.pick_a_product(0)
        product3_name = self.Product_Page.product_name_text()
        print(product3_name)
        sleep(2)
        quantity3 = self.Product_Page.change_quantity("1")
        sleep(2)
        self.Product_Page.click_add_to_cart()
        self.Logo_Section.cart_icon()
        print(self.Logo_Section.name_of_products_in_cart_text(2))
        print(self.Logo_Section.name_of_products_in_cart_text(1))
        print(self.Logo_Section.name_of_products_in_cart_text(0))

        self.Logo_Section.cart_icon()

        self.assertIn(self.Logo_Section.name_of_products_in_cart_text(2),product1_name)
        self.assertIn(self.Logo_Section.name_of_products_in_cart_text(1),product2_name)
        self.assertIn(self.Logo_Section.name_of_products_in_cart_text(0),product3_name)

        print(self.Logo_Section.quantity_of_product_in_cart(0))
        print(self.Logo_Section.quantity_of_product_in_cart(1))
        print(self.Logo_Section.quantity_of_product_in_cart(2))
        self.assertEqual(self.Logo_Section.quantity_of_product_in_cart(0),quantity3)

        self.assertEqual(self.Logo_Section.quantity_of_product_in_cart(2),quantity1)
        self.assertEqual(self.Logo_Section.quantity_of_product_in_cart(1), quantity2)

















