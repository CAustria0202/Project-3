from selenium.webdriver.common.by import By
from Data.locators import TopBarLocators
from Base.base_driver import BaseDriver

class TopNavigationBar(BaseDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_currency_button(self):
        self.wait_until_element_to_be_clickable(By.CSS_SELECTOR, TopBarLocators.CURRENCY_BUTTON).click()

    def change_currency(self, currency_type):
        currency = self.wait_for_presence_of_all_elements(By.XPATH, TopBarLocators.CURRENCY_DROPDOWN)
        for element in currency:
            if element.text == currency_type:
                print(f"Element Text: {element.text}")
                element.click()
                break

    def change_price_tag_currency(self, text_value):
        self.wait_until_text_to_be_present(By.XPATH, TopBarLocators.PRICE_TAGS, text_value)
        tags = self.wait_for_presence_of_all_elements(By.XPATH, TopBarLocators.PRICE_TAGS)

        updated_price_tags = []

        if isinstance(tags, list):
            for tag in tags:
                price_text = tag.text.strip()
                updated_price_tags.append(price_text)
                print("Updated Price Text:", price_text)
        else:
            updated_price_tags.append(tags.text.strip())
            print("Updated Price Text:", tags.text.strip())

        return updated_price_tags

    def click_telephone(self):
        self.wait_for_presence_of_the_element(By.CSS_SELECTOR, TopBarLocators.TELEPHONE_ICON).click()

    def click_my_account(self):
        self.wait_until_element_to_be_clickable(By.CSS_SELECTOR, TopBarLocators.MY_ACCOUNT_BUTTON).click()

    def my_account_options(self,account_drpdwn):
        account = self.wait_for_presence_of_all_elements(By.XPATH, TopBarLocators.MY_ACCOUNT_DROPDOWN)

        for element in account:
            if element.text == account_drpdwn:
                print(f"Element Text: {element.text}")
                element.click()
                break

    def click_wishlist(self):
        self.wait_until_element_to_be_clickable(By.ID, TopBarLocators.WISHLIST).click()

    def click_shopping_cart(self):
        self.wait_until_element_to_be_clickable(By.CSS_SELECTOR, TopBarLocators.SHOPPING_CART).click()

    def click_checkout(self):
        self.wait_until_element_to_be_clickable(By.CSS_SELECTOR, TopBarLocators.CHECKOUT).click()