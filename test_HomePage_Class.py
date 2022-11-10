from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Category_Page import Category_Page
from HomePage_Class import HomePage
from Product_Page import Product_Page
from ShoppingCart_Page import ShoppingCart
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
        self.Shopping_Cart = ShoppingCart(self.driver)

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
        self.Logo_Section.cart_icon_hover()
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
        # print(product1_name)
        """index zero does not show the correct color"""
        self.Product_Page.colors_list()
        color1 = self.Product_Page.colors_list_text(0)


        self.Product_Page.click_on_color(0)
        print(color1)
        #sleep(2)
        quantity1 = self.Product_Page.change_quantity("2")
        #sleep(2)
        self.Product_Page.click_add_to_cart()
        #sleep(2)

        # price1 = self.Product_Page.product_price_text_to_float()
        # quantity = self.Logo_Section.change_to_int_quantity_of_product(2)
        # total = price1 * quantity
        #
        # self.assertEqual(self.Logo_Section.price_of_each_product_to_float(2), total)

        self.Navigation_Bar.click_homepage_button()
        self.Home_Page.category_click(1)
        #sleep(2)
        self.Category_Page.pick_a_product(1)
        product2_name = self.Product_Page.product_name_text()
        self.Product_Page.colors_list()
        # print(product2_name)

        color2 = self.Product_Page.colors_list_text(1)
        # self.Product_Page.click_on_color(1)
        print(color2)
        #sleep(2)
        quantity2 = self.Product_Page.change_quantity("3")

        self.Product_Page.click_add_to_cart()

        # price1 = self.Product_Page.product_price_text_to_float()
        # quantity = self.Logo_Section.change_to_int_quantity_of_product("3")
        # total = price1 * quantity
        #
        # self.assertEqual(self.Logo_Section.price_of_each_product_to_float(1), total)

        self.Navigation_Bar.click_homepage_button()
        self.Home_Page.category_click(3)
        sleep(2)
        self.Category_Page.pick_a_product(0)
        product3_name = self.Product_Page.product_name_text()
        self.Product_Page.colors_list()
        # print(product3_name)
        color3 = self.Product_Page.colors_list_text(0)
        # self.Product_Page.click_on_color(0)
        print(color3)
        sleep(2)
        quantity3 = self.Product_Page.change_quantity("1")
        sleep(2)
        self.Product_Page.click_add_to_cart()

        price1 = self.Product_Page.product_price_text_to_float()
        quantity = self.Logo_Section.change_to_int_quantity_of_product("1")
        total = price1 * quantity

        self.assertEqual(self.Logo_Section.price_of_each_product_to_float(0), total)
        self.Logo_Section.cart_icon_hover()
        # print(self.Logo_Section.name_of_products_in_cart_text(2))
        # print(self.Logo_Section.name_of_products_in_cart_text(1))
        # print(self.Logo_Section.name_of_products_in_cart_text(0))

        self.Logo_Section.cart_icon_hover()


        #check the name
        self.assertIn(self.Logo_Section.name_of_products_in_cart_text(2),product1_name)
        self.assertIn(self.Logo_Section.name_of_products_in_cart_text(1),product2_name)
        self.assertIn(self.Logo_Section.name_of_products_in_cart_text(0),product3_name)


        #checks the quantity

        # print(self.Logo_Section.quantity_of_product_in_cart(0))
        # print(self.Logo_Section.quantity_of_product_in_cart(1))
        # print(self.Logo_Section.quantity_of_product_in_cart(2))
        # self.assertEqual(self.Logo_Section.quantity_of_product_in_cart(0),quantity3)
        # self.assertEqual(self.Logo_Section.quantity_of_product_in_cart(2),quantity1)
        # self.assertEqual(self.Logo_Section.quantity_of_product_in_cart(1), quantity2)

        #check the color

        print(self.Logo_Section.colors_of_products_in_cart(2))
        print(self.Logo_Section.colors_of_products_in_cart(1))
        print(self.Logo_Section.colors_of_products_in_cart(0))
        # self.assertEqual()

        #check the price
        # price1= self.Product_Page.product_price_text_to_float()
        # quantity = self.Logo_Section.change_to_int_quantity_of_product()
        # total = price1 * quantity
        #
        # self.assertEqual(self.Logo_Section.price_of_each_product_to_float(),total)

        # print(self.Product_Page.total_price_for_each_product(self.Product_Page.change_quantity()))


    def testcase3(self):
        self.Home_Page.category_click(0)
        self.Category_Page.pick_a_product(2)
        sleep(2)
        quantity1 = self.Product_Page.change_quantity("3")
        sleep(2)
        self.Product_Page.click_add_to_cart()
        sleep(2)
        self.Navigation_Bar.click_homepage_button()
        self.Home_Page.category_click(2)
        sleep(2)
        self.Category_Page.pick_a_product(1)
        name_of_recent_product = self.Product_Page.product_name_text()
        sleep(2)
        quantity2 = self.Product_Page.change_quantity("2")
        sleep(2)
        self.Product_Page.click_add_to_cart()

        self.Logo_Section.cart_icon_hover()

        self.Logo_Section.click_on_remove_item_from_the_cart(0)
        self.Logo_Section.cart_icon_hover()

        self.assertNotIn(name_of_recent_product,self.Logo_Section.name_of_products_in_cart_text(0))
        print(name_of_recent_product)
        print(self.Logo_Section.name_of_products_in_cart_text(0))


    def testcase4(self):
        self.Home_Page.category_click(0)
        self.Category_Page.pick_a_product(0)
        sleep(2)
        quantity1 = self.Product_Page.change_quantity("2")
        sleep(2)
        self.Product_Page.click_add_to_cart()
        sleep(2)

        self.Logo_Section.click_cart_icon()

        self.assertEqual(self.Shopping_Cart.shopping_cart_location_text(),"SHOPPING CART")





































