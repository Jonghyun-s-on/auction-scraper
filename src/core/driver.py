from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from src.config.config import CHROME_DRIVER_PATH

_driver = None


def get_driver(headless=True):
    global _driver
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    service = Service(executable_path=CHROME_DRIVER_PATH)
    _driver = webdriver.Chrome(service=service, options=options)
    return _driver


def close_driver():
    global _driver
    if _driver:
        _driver.quit()
        _driver = None
