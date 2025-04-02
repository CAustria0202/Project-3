import pytest
from Base.base_driver import BaseDriver
from Pages.login_page import LoginPage
from Pages.register_page import RegisterPage
from Pages.top_navigation_bar import TopNavigationBar
from Pages.contact_us_page import ContactUsPage
from Pages.shopping_cart_page import ShoppingCartPage
from Utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class TestTopNavigationBar:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.navbar = TopNavigationBar(self.driver)
        self.contact = ContactUsPage(self.driver)
        self.register = RegisterPage(self.driver)
        self.login = LoginPage(self.driver)
        self.shop = ShoppingCartPage(self.driver)
        self.base_drive = BaseDriver(self.driver)
        self.utils = Utils(self.driver)

    @pytest.mark.parametrize("selected_currency, currency", [
        ("€ Euro", "€"),
        ("£ Pound Sterling", "£"),
        ("$ US Dollar", "$")
    ])
    def test_changing_currency(self, selected_currency, currency):
        self.navbar.click_currency_button()
        self.navbar.change_currency(selected_currency)
        tags = self.navbar.change_price_tag_currency(currency)
        for tag in tags:
            Utils.assert_element_to_have_text(currency, tag)

    def test_clicking_telephone(self):
        self.navbar.click_telephone()

        contact_header_element = self.contact.locate_contact_header()
        Utils.assert_element_exists(contact_header_element, "Contact header not found on the Page")

        Utils.assert_element_text("Contact Us", contact_header_element.text)

    @pytest.mark.parametrize("account_option", ["Register", "Login"])
    def test_my_account(self, account_option):
        self.navbar.click_my_account()
        self.navbar.my_account_options(account_option)

        if account_option == "Register":
            register_header_element = self.register.locate_register_header()
            Utils.assert_element_exists(register_header_element, "Register header not found on the Page")

            Utils.assert_element_text("Register Account", register_header_element.text)
        elif account_option == "Login":
            login_header_element = self.login.locate_login_header()
            Utils.assert_element_exists(login_header_element, "Register header not found on the Page")

            Utils.assert_element_text("New Customer", login_header_element.text)
        else:
            print(f"The Selected {account_option} is not available.")


    def test_clicking_wishlist(self):
        self.navbar.click_wishlist()

        login_header_element = self.login.locate_login_header()
        Utils.assert_element_exists(login_header_element, "Login header not found on the Page")

        Utils.assert_element_text("New Customer", login_header_element.text)

    def test_clicking_shopping_cart(self):
        self.navbar.click_shopping_cart()

        cart_header_element = self.shop.locate_shopping_cart_header()
        Utils.assert_element_exists(cart_header_element, "Shopping Cart header not found on the Page")

        Utils.assert_element_text("Shopping Cart", cart_header_element.text)

    def test_clicking_checkout(self):
        self.navbar.click_checkout()

        cart_header_element = self.shop.locate_shopping_cart_header()
        Utils.assert_element_exists(cart_header_element, "Shopping Cart header not found on the Page")

        Utils.assert_element_text("Shopping Cart", cart_header_element.text)

