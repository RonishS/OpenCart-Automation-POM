from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")
    FIRST_PRODUCT = (By.XPATH, "(//div[@class='product-thumb'])[1]")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(.,'Add to Cart')]")
    CART_ICON = (By.ID, "cart-total")
    
    def is_logout_visible(self):
        return self.is_visible(self.LOGOUT_LINK)
    
    def select_first_product(self):
        self.click(self.FIRST_PRODUCT)
    
    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
    
    def open_cart(self):
        self.click(self.CART_ICON)
