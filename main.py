import sys
from src.config.condition import CONDITION
from src.core.driver import get_driver, close_driver
from src.core.fetcher import fetch_pages
from src.utils.form_util import generate_valid_forms
from src.utils.logger import logger


def main():
    try:
        # 1. Chrome Driver 실행 (headless=False → Web Browser 표시)
        driver = get_driver(False)

        # 2. 유효한 검색 조건(form) 만큼 반복
        for form in generate_valid_forms(CONDITION):
            # 각 조건(form)을 적용한 결과 페이지 전체를 HTML 로 수집
            page_source = fetch_pages(driver, form)
    except Exception as e:
        logger.exception(f"{e}")
        sys.exit(1)
    finally:
        close_driver()


if __name__ == '__main__':
    main()
