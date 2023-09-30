import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver.


class Base_driver:
    def __init__(self,driver):
        self.driver=driver

    def scroll_page(self,direction):
        page_legth=self.driver.execute_script("windows.scrollTo(0,document.body.scrollHeight)")
        match=False
        while (match==False):
            last_count=page_legth
            time.sleep((3))
            page_legth = self.driver.execute_script("windows.scrollTo(0,document.body.scrollHeight)")
            if last_count==page_legth:
                match=True

    def wait_until_presence_of_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element=wait.until(
            Ec.presence_of_element_located((getattr(By, locator_type), locator)))
        return element

    def element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element=wait.until(
            Ec.element_to_be_clickable((getattr(By, locator_type), locator)))
        return element




