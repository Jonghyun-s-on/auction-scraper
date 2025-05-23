from scraper.driver import get_driver, close_driver
from scraper.fetcher import fetch_page
from form.selector_parser import build_forms_from_selector_module

def main():
    try:
        driver = get_driver(False)

        for form in build_forms_from_selector_module():
            print(form)
            page_source = fetch_page(driver, form)
            print(page_source)
    finally:
        close_driver()

if __name__ == '__main__':
    main()
