from pages.login_page import LoginPage

def test_login_invalid(driver):
    driver.get("https://www.saucedemo.com/")
    login = LoginPage(driver)
    login.login("wrong_user", "wrong_pass")
    assert "Epic sadface" in login.get_error()