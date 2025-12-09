from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")

    inv = InventoryPage(driver)
    inv.add_first_product()
    inv.go_to_cart()

    cart = CartPage(driver)
    cart.checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_data("Juan", "Pérez", "1234")
    checkout.finish_purchase()

    assert "Thank you" in checkout.get_confirmation()