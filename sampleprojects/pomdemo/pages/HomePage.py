""""
Hosts simple action from home page at:
https://opensource-demo.orangehrmlive.com/index.php/dashboard

which shows up after login from:
https://opensource-demo.orangehrmlive.com/
using credential: Admin / admin123
"""
from sampleprojects.pomdemo.locators.Locators import Locators


class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def click_welcome_admin_link(self):
        self.driver.find_element_by_link_text(Locators.home_welcome_admin_link_text).click()

    def click_logout_link(self):
        self.driver.find_element_by_link_text(Locators.home_logout_link_text).click()