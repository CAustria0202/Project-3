class TopBarLocators:
    #BY CSS SELECTOR
    CURRENCY_BUTTON = ".btn.btn-link.dropdown-toggle"
    TELEPHONE_ICON = ".fa.fa-phone"
    MY_ACCOUNT_BUTTON = "a[title='My Account']"
    SHOPPING_CART = "a[title='Shopping Cart']"
    CHECKOUT = "a[title='Checkout']"

    #BY XPATH
    CURRENCY_DROPDOWN = "//ul[@class='dropdown-menu']//li"
    MY_ACCOUNT_DROPDOWN = "//ul[@class='dropdown-menu dropdown-menu-right']//li"
    PRICE_TAGS = "//p[contains(@class, 'price')]"

    #BY ID
    WISHLIST = "wishlist-total"

class ContactLocators:

    CONTACT_HEADER = "div[id='content'] h1"

class FooterLocators:

    #Information Section
    ABOUT_US = "//a[normalize-space()='About Us']"
    DELIVERY_INFO = "//a[normalize-space()='Delivery Information']"
    PRIVACY_POLICY = "//a[normalize-space()='Privacy Policy']"
    TERMS = "//a[normalize-space()='Terms & Conditions']"

    #Customer Service
    CONTACT_US = "//a[normalize-space()='Contact Us']"
    RETURNS = "//a[normalize-space()='Returns']"
    SITE_MAP = "//a[normalize-space()='Site Map']"

    #Extra
    BRANDS = "//a[normalize-space()='Brands']"
    GIFT = "//a[normalize-space()='Gift Certificates']"
    AFFILIATE = "//a[normalize-space()='Affiliate']"
    SPECIALS = "//a[normalize-space()='Specials']"

    #My Account
    MY_ACCOUNT = "//a[contains(text(),'My Account')]"
    ORDER_HISTORY = "//a[normalize-space()='Order History']"
    WISHLIST = "//a[normalize-space()='Wish List']"
    NEWSLETTER = "//a[normalize-space()='Newsletter']"

class LoginLocators:

    LOGIN_HEADER = "//h2[normalize-space()='New Customer']"

class RegisterLocators:
    REGISTER_HEADER = "div[id='content'] h1"

class ShoppingCartLocator:
    SHOPPING_CART_HEADER = "div[id='content'] h1"

class ProductReturnLocators:
    RETURN_HEADER = "div[id='content'] h1"

class SiteMapLocators:
    SITE_MAP = "div[id='content'] h1"