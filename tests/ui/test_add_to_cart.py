from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_product(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_first_product()
    inventory.go_to_cart()

    assert "cart" in driver.current_url