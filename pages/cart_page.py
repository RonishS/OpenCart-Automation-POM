from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.LINK_TEXT, "Checkout")
    CART_ITEMS = (By.XPATH, "//div[@class='table-responsive']//tbody/tr")
    
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
    
    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))
