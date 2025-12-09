from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def fill_data(self, name, last, zip_code):
        self.type(self.FIRST_NAME, name)
        self.type(self.LAST_NAME, last)
        self.type(self.ZIP, zip_code)
        self.click(self.CONTINUE_BTN)

    def finish_purchase(self):
        self.click(self.FINISH_BTN)

    def get_confirmation(self):
        return self.get_text(self.COMPLETE_HEADER)