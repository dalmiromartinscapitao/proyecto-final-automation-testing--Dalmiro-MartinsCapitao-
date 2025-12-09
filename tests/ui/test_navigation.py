from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_navigation_inventory(driver):
    driver.get("https://www.saucedemo.com/")
    LoginPage(driver).login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.get_title() == "Products"