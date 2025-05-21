from scraper.driver import get_driver, close_driver
from scraper.fetcher import fetch_page

def main():
    try:
        driver = get_driver(False)
        page_source = fetch_page(driver)
        print(page_source)
    finally:
        close_driver()

if __name__ == '__main__':
    main()