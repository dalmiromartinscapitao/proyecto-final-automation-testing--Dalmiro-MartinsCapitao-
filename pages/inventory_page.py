from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):

    TITLE = (By.CLASS_NAME, "title")
    FIRST_ADD_BTN = (By.CSS_SELECTOR, ".inventory_item button")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_first_product(self):
        self.click(self.FIRST_ADD_BTN)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_title(self):
        return self.get_text(self.TITLE)