import logging

# "auction-scraper"라는 이름의 전역 로거 객체 생성
logger = logging.getLogger("auction-scraper")

# 로그 레벨 설정: INFO 이상만 출력 (INFO, WARNING, ERROR 등)
logger.setLevel(logging.INFO)

# 핸들러 중복 추가 방지: 기존 핸들러가 없을 경우에만 설정
if not logger.hasHandlers():
    # 콘솔 출력용 핸들러 생성 (stdout)
    handler = logging.StreamHandler()

    # 로그 메시지 포맷 지정: [LEVEL] timestamp - message
    formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
    handler.setFormatter(formatter)

    # 로거에 핸들러 추가
    logger.addHandler(handler)
