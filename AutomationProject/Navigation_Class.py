from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Navigation:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

# should we make the category general?
    def navigation_category_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "redirect('/category/' + breadCrumbCategoryName + '/' + product.categoryId)")

    def click_navigation_category_button(self):
        self.navigation_category_button().click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "categoryTitle roboto-regular sticky ng-binding")))

    def homepage_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class = 'ng-scope'][translate = 'HOME']")

    def click_homepage_button(self):
        self.homepage_button().click()