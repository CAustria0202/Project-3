from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Data.locators import ContactLocators

class ContactUsPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def locate_contact_header(self):
        return self.wait_for_presence_of_the_element(By.CSS_SELECTOR, ContactLocators.CONTACT_HEADER)
