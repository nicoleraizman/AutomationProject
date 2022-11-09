from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Category_Page import Category_Page
from HomePage_Class import HomePage
from Navigation_Class import Navigation
from time import sleep


class testAOS(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\selenium1\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service_chrome)

        self.driver.get("https://petstore.octoperf.com/actions/Catalog.action")

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

