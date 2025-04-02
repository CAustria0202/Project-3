from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Data.locators import RegisterLocators

class RegisterPage(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def locate_register_header(self):
        return self.wait_for_presence_of_the_element(By.CSS_SELECTOR, RegisterLocators.REGISTER_HEADER)
