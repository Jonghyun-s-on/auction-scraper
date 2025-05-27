from core.driver import get_driver, close_driver
from core.fetcher import fetch_page
from utils.form_generator import generate_form_list

from config.selector import SELECTOR
from config.condition import CONDITION

def main():
    try:
        driver = get_driver(False)
        for form in generate_form_list(CONDITION):
            page_source = fetch_page(driver, form)
            print(page_source)
    finally:
        close_driver()

if __name__ == '__main__':
    main()
