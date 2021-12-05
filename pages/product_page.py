from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart.click()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON)

    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_title_of_product_added_to_cart(self):
        return self.browser.find_element(*ProductPageLocators.IN_CART_PRODUCT_TITLE).text

    def get_price_of_product_added_to_cart(self):
        return self.browser.find_element(*ProductPageLocators.IN_CART_TOTAL_PRICE).text

    def title_of_added_product_should_be_correct(self, title):
        assert title == self.get_title_of_product_added_to_cart() , "Product title is wrong"

    def price_of_added_product_should_be_correct(self, price):
        assert price == self.get_price_of_product_added_to_cart(), "Product price is wrong"

    def price_and_title_of_added_product_should_be_correct(self, title, price):
        self.price_of_added_product_should_be_correct(price)
        self.title_of_added_product_should_be_correct(title)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message  have not disappeared, but should"
