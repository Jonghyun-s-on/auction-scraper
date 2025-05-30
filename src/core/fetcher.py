from src.config.config import BASE_URL, SEARCH_URI
from src.config.selector import FORM_SELECTOR, RESULT_SELECTOR
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep


def fetch_pages(driver, form_dict):
    search_data(driver, form_dict)
    htmls = scrape_pages(driver)

    for html in htmls:
        print(html)

    return htmls


def search_data(driver, form_dict):
    driver.get(BASE_URL + SEARCH_URI)
    sleep(2)

    for key, value in form_dict.items():
        handle_input(driver, FORM_SELECTOR[key], value)

    handle_input(driver, FORM_SELECTOR["submit_button"])
    sleep(2)

def scrape_pages(driver):
    # 페이지 당 데이터 수를 10 -> 40 으로 변경
    handle_input(driver, RESULT_SELECTOR["page_size_input"], "40")
    sleep(5)

    html_pages = []
    result_sel = RESULT_SELECTOR["content_box"]

    while True:
        try:
            result_element = driver.find_element(result_sel["by"], result_sel["value"])
            html_pages.append(result_element.get_attribute("outerHTML"))
        except NoSuchElementException:
            break

        try:
            current = driver.find_element(By.CSS_SELECTOR, "a.w2pageList_label_selected")
            current_index = int(current.get_attribute("data-index"))
        except NoSuchElementException:
            break

        # 3. 다음 페이지가 있으면 클릭
        try:
            # 다음 번호 a[data-index=+1] 있는지 먼저 시도
            next_page = driver.find_element(By.CSS_SELECTOR, f"a[data-index='{current_index + 1}']")
            next_page.click()
            sleep(2)
            continue
        except Exception:
            pass  # 다음 번호가 없으면 → 블록 이동 시도

        # 4. 다음 블록 버튼 클릭 후 실제로 페이지가 넘어갔는지 확인
        try:
            next_btn = driver.find_element(By.ID, "mf_wfm_mainFrame_pgl_gdsDtlSrchPage_next_btn").find_element(By.TAG_NAME, "button")
            next_btn.click()
            sleep(2)

            # 페이지 이동 여부 재확인
            new_index = int(driver.find_element(By.CSS_SELECTOR, "a.w2pageList_label_selected").get_attribute("data-index"))
            if new_index <= current_index:
                break  # 변화 없음 → 끝
        except Exception:
            break  # 다음 블록 버튼 없음 → 종료

    return html_pages


def handle_input(driver, selector: dict, value=None):
    input_type = selector["type"]

    if input_type == "select":
        element = driver.find_element(selector["by"], selector["value"])
        Select(element).select_by_visible_text(value)

    elif input_type == "text":
        element = driver.find_element(selector["by"], selector["value"])
        element.clear()
        element.send_keys(value)

    elif input_type == "radio":
        option_selector = selector["options"][value]
        element = driver.find_element(selector["by"], option_selector)
        element.click()

    elif input_type == "button":
        element = driver.find_element(selector["by"], selector["value"])
        element.click()