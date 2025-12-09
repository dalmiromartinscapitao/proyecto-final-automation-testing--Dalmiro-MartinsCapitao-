import pytest
import datetime
from selenium import webdriver
from utils.logger import logger

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# ⬇ Nueva forma de capturar fallos en pytest 8+
def pytest_runtest_makereport(item, call):
    if call.when == "call":  # fase donde se ejecuta la prueba
        if call.excinfo is not None:  # si hubo una excepción → prueba falló
            driver = item.funcargs.get("driver")
            if driver:
                screenshot_name = f"{item.name}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                path = f"./screenshots/{screenshot_name}"
                driver.save_screenshot(path)
                logger.error(f"Test FAILED → Screenshot guardado: {path}")