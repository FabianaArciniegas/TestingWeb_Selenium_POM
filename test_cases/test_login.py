import os
import sys
import unittest

import HtmlTestRunner
from ddt import ddt, file_data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

sys.path.append(r"D:\Users\Dennys\Documents\proyectos_programacion\Testing_QA\TutorialSeleniumPOM")

from page_objects.login_page import LoginPage


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        service = Service("../drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(options=chrome_options, service=service)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        cls.login_page = LoginPage(driver=cls.driver)
        cls.driver.implicitly_wait(time_to_wait=10)

    @file_data(os.path.join("data", "test_login.json"))
    def test_login_valido(self, username, password):
        self.login_page.login_in_app(username=username, password=password)
        is_login_successful = self.login_page.is_login_successful()

        # Assertions
        self.assertTrue(is_login_successful)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output="../reports"))
