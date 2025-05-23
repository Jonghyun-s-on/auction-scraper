from scraper.config import BASE_URL, SEARCH_URI
from scraper.selector import *
from selenium.webdriver.support.ui import Select
import time

def fetch_page(driver, form):
    court = form.fields["court"]
    bid_type = form.fields["bid_type"]
    submit = form.fields["submit"]

    # 검색 페이지 접속
    driver.get(BASE_URL + SEARCH_URI)
    time.sleep(2)

    # 법원 선택
    select_option(driver, court["selector"], court["value"])
    time.sleep(2)

    # 입찰 구분 선택
    click_element(driver, bid_type["selector"])
    time.sleep(2)

    # 검색 버튼 클릭
    click_element(driver, submit["selector"])
    time.sleep(5)

    return driver.page_source

def click_element(driver, selector):
    selected_element = driver.find_element(*selector)
    selected_element.click()

def select_option(driver, selector, value):
    selected_element = driver.find_element(*selector)
    select_box = Select(selected_element)
    select_box.select_by_visible_text(value)