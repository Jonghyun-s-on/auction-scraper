from config.config import BASE_URL, SEARCH_URI
from selenium.webdriver.support.ui import Select
import time

def fetch_page(driver, form):
    print(form)
    return form

# def click_element(driver, selector):
#     selected_element = driver.find_element(*selector)
#     selected_element.click()
#
# def select_option(driver, selector, value):
#     selected_element = driver.find_element(*selector)
#     select_box = Select(selected_element)
#     select_box.select_by_visible_text(value)