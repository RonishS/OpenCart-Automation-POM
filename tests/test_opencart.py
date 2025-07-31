import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage

def test_full_flow(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    cart_page = CartPage(browser)
    
    TEST_EMAIL = "test@example.com"
    TEST_PASSWORD = "password123"
    
    login_page.open_login_page()
    login_page.login(TEST_EMAIL, TEST_PASSWORD)
    assert home_page.is_logout_visible(), "Login failed!"
    
    home_page.select_first_product()
    home_page.add_to_cart()
    home_page.open_cart()
    assert cart_page.get_cart_item_count() > 0, "Cart is empty!"
    
    cart_page.proceed_to_checkout()
    assert "checkout" in browser.current_url, "Not on checkout page!"
    print("\nTEST PASSED!")
