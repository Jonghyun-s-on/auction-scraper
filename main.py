from src.core.driver import get_driver, close_driver
from src.core.fetcher import fetch_pages
from src.utils.form_util import generate_form_list, is_valid_form
from src.config.condition import CONDITION


def main():
    try:
        driver = get_driver(False)
        for form in generate_form_list(CONDITION):
            if is_valid_form(form):
                page_source = fetch_pages(driver, form)
                print(page_source)
    finally:
        close_driver()


if __name__ == '__main__':
    main()
