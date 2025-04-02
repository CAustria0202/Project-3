import pytest
from Base.base_driver import BaseDriver
from Pages.contact_us_page import ContactUsPage
from Pages.footer_section import FooterSection
from Pages.product_returns import ProductReturns
from Pages.site_map_page import SiteMap
from Utilities.utils import Utils

@pytest.mark.usefixtures("setup")
class TestFooter:

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.driver = setup
        self.base_drive = BaseDriver(self.driver)
        self.contact = ContactUsPage(self.driver)
        self.footer = FooterSection(self.driver)
        self.prd_returns = ProductReturns(self.driver)
        self.map = SiteMap(self.driver)
        self.utils = Utils(self.driver)

        # Automatically wait for the page to load before every test
        self.utils.wait_for_page_load()

    def test_about_us(self):
        self.footer.click_footer_about_us()  # Click and return driver
        self.utils.assert_page_contains_text("About Us")

    def test_delivery_info(self):
        self.footer.click_footer_delivery_info()
        self.utils.assert_page_contains_text("Delivery Information")

    def test_privacy_policy(self):
        self.footer.click_footer_privacy_policy()
        self.utils.assert_page_contains_text("Privacy Policy")

    def test_terms_and_conditions(self):
        self.footer.click_footer_terms()
        self.utils.assert_page_contains_text("Terms & Conditions")

    def test_contact_us(self):
        self.footer.click_footer_contact_us()

        contact_header_element = self.contact.locate_contact_header()
        Utils.assert_element_exists(contact_header_element, "Contact header not found on the Page")

        Utils.assert_element_text("Contact Us", contact_header_element.text)

    def test_returns(self):
        self.footer.click_footer_returns()

        prd_header_element = self.prd_returns.locate_product_return_header()
        Utils.assert_element_exists(prd_header_element, "Product Returns header not found on the Page")

        Utils.assert_element_text("Product Returns", prd_header_element.text)

    def test_site_map(self):
        self.footer.click_footer_site_map()

        map_header_element = self.map.locate_site_map_header()
        Utils.assert_element_exists(map_header_element, "Site Map header not found on the Page")

        Utils.assert_element_text("Site Map", map_header_element.text)