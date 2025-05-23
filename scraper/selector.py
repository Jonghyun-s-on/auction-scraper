from selenium.webdriver.common.by import By

SEARCH_SUBMIT_SELECTOR = (By.ID, "mf_wfm_mainFrame_btn_gdsDtlSrch")

# 검색 조건 정보
#   법원
SEARCH_COURT_SELECTOR = (By.ID, "mf_wfm_mainFrame_sbx_rletCortOfc")
SEARCH_COURT_VALUES = ['서울중앙지방법원', '서울동부지방법원', '서울서부지방법원']
SEARCH_COURT_INPUT_TYPE = 'select'

#   입찰 구분
SEARCH_BID_TYPE_SELECTOR = (By.CSS_SELECTOR, "label[for='mf_wfm_mainFrame_rad_mvprpBidLst_input_2']")
SEARCH_BID_TYPE_INPUT_TYPE = 'radio'

#   기간
SEARCH_START_DATE_SELECTOR = (By.ID, "mf_wfm_mainFrame_cal_rletPerdStr_input")
SEARCH_START_DATE_VALUE = "20250522"
SEARCH_START_DATE_INPUT_TYPE = 'text'
SEARCH_END_DATE_SELECTOR = (By.ID, "mf_wfm_mainFrame_cal_rletPerdEnd_input")
SEARCH_END_DATE_VALUE = "20250523"
SEARCH_END_DATE_INPUT_TYPE = 'text'

#   용도
SEARCH_USAGE_LV1_SELECTOR = (By.ID, "mf_wfm_mainFrame_sbx_rletLclLst")
SEARCH_USAGE_LV1_VALUE = "토지"
SEARCH_USAGE_LV1_INPUT_TYPE = 'select'
SEARCH_USAGE_LV2_SELECTOR = (By.ID, "mf_wfm_mainFrame_sbx_rletMclLst")
SEARCH_USAGE_LV2_VALUE = "지목"
SEARCH_USAGE_LV2_INPUT_TYPE = 'select'
SEARCH_USAGE_LV3_SELECTOR = (By.ID, "mf_wfm_mainFrame_sbx_rletSclLst")
SEARCH_USAGE_LV3_VALUES = ["대지"]
SEARCH_USAGE_LV3_INPUT_TYPE = 'select'
