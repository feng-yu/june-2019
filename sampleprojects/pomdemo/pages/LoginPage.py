"""
simulate all the action that can be taken from login page at:
https://opensource-demo.orangehrmlive.com/index.php/auth/login
"""
from sampleprojects.pomdemo.locators.Locators import Locators


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_id(Locators.login_username_text_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(Locators.login_password_text_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id(Locators.login_login_button_id).click()

    def click_forgot_password_link(self):
        self.driver.find_element_by_id(Locators.login_forgot_password_link_text).click()

    def get_invalid_credential_message(self):
        elem = self.driver.find_element_by_xpath(Locators.login_invalid_credential_message)
        return elem.text