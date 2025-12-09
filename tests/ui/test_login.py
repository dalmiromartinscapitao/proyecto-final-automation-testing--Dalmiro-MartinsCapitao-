import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce")
])
def test_login_success(driver, username, password):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.login(username, password)
    assert "inventory" in driver.current_url