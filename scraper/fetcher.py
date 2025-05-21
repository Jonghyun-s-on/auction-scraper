from config.settings import BASE_URL, SEARCH_URI, SEARCH_BUTTON_ID
from selenium.webdriver.common.by import By
import time

def fetch_page(driver):
    driver.get(BASE_URL + SEARCH_URI)
    time.sleep(5)

    search_button = driver.find_element(By.ID, SEARCH_BUTTON_ID)
    search_button.click()
    time.sleep(5)

    return driver.page_source