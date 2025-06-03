from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from src.config.config import CHROME_DRIVER_PATH

_driver = None  # 전역 Driver 인스턴스


def get_driver(headless=True):
    global _driver

    options = Options()

    # 헤드리스 모드 설정
    if headless:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")

    # 창 사이즈 고정 (화면 불일치 이슈 방지)
    options.add_argument("--window-size=1920,1080")

    # Chrome Driver 경로 지정
    service = Service(executable_path=CHROME_DRIVER_PATH)

    # Chrome Driver 실행
    _driver = webdriver.Chrome(service=service, options=options)
    return _driver


def close_driver():
    global _driver
    if _driver:
        _driver.quit()
        _driver = None
