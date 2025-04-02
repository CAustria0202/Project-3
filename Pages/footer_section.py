from selenium.webdriver.common.by import By
from Base.base_driver import BaseDriver
from Data.locators import FooterLocators
class FooterSection(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_footer_about_us(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.ABOUT_US).click()

    def click_footer_delivery_info(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.DELIVERY_INFO).click()

    def click_footer_privacy_policy(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.PRIVACY_POLICY).click()

    def click_footer_terms(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.TERMS).click()

    def click_footer_contact_us(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.CONTACT_US).click()

    def click_footer_returns(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.RETURNS).click()

    def click_footer_site_map(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.SITE_MAP).click()

    def click_footer_brands(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.BRANDS).click()

    def click_footer_gift(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.GIFT).click()

    def click_footer_affiliate(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.AFFILIATE).click()

    def click_footer_specials(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.SPECIALS).click()

    def click_footer_my_account(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.MY_ACCOUNT).click()

    def click_footer_order_history(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.ORDER_HISTORY).click()

    def click_footer_wishlist(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.WISHLIST).click()

    def click_footer_newsletter(self):
        self.wait_for_presence_of_the_element(By.XPATH, FooterLocators.NEWSLETTER).click()