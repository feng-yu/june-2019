"""
Test the login age at:
https://opensource-demo.orangehrmlive.com
"""
from selenium import webdriver
import HtmlTestRunner
import unittest
import time
from sampleprojects.pomdemo.pages.LoginPage import LoginPage
from sampleprojects.pomdemo.pages.HomePage import HomePage


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('C:/Tools/Selenium/chromedriver_win32/chromedriver_74.exe')
        cls.driver.implicitly_wait(10)

    def test_login_page_valid(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        login_page = LoginPage(self.driver)
        login_page.enter_username('Admin')
        login_page.enter_password('admin123')
        login_page.click_login_button()

        time.sleep(1)

        home_page = HomePage(self.driver)
        home_page.click_welcome_admin_link()
        home_page.click_logout_link()

        time.sleep(2)

    def test_login_page_invalid(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com')
        login_page = LoginPage(self.driver)
        login_page.enter_username('Admin1')
        login_page.enter_password('admin123')
        login_page.click_login_button()

        message = login_page.get_invalid_credential_message()
        self.assertEqual(message, 'Invalid credentials')

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('Test completed!')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/User/PycharmProjects/june-2019/sampleprojects/pomdemo/reports'))

