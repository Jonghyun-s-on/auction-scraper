from selenium.webdriver.common.by import By

SEARCH_BUTTON_SELECTOR = (By.ID, "mf_wfm_mainFrame_btn_gdsDtlSrch")

# 검색 조건 정보
#   법원
SEARCH_COURT_INPUT_SELECTOR = (By.ID, "mf_wfm_mainFrame_sbx_rletCortOfc")
SEARCH_COURT_INPUT_VALUES = ['서울중앙지방법원', '서울동부지방법원', '서울서부지방법원']

#   입찰 구분
SEARCH_BID_TYPE_SELECTOR = (By.CSS_SELECTOR, "label[for='mf_wfm_mainFrame_rad_mvprpBidLst_input_2']")

#   기간
SEARCH_START_DATE_INPUT_SELECTOR = (By.ID, "mf_wfm_mainFrame_cal_rletPerdStr_input")
SEARCH_START_DATE_INPUT_VALUE = "20250522"
SEARCH_END_DATE_INPUT_SELECTOR = (By.ID, "mf_wfm_mainFrame_cal_rletPerdEnd_input")
SEARCH_END_DATE_INPUT_VALUE = "20250523"

#   용도
SEARCH_USAGE_LV1_INPUT_SELECTOR = "mf_wfm_mainFrame_sbx_rletLclLst"
SEARCH_USAGE_LV1_INPUT_VALUES = ["토지"]
SEARCH_USAGE_LV2_INPUT_SELECTOR = "mf_wfm_mainFrame_sbx_rletMclLst"
SEARCH_USAGE_LV2_INPUT_VALUES = ["지목"]
SEARCH_USAGE_LV3_INPUT_SELECTOR = "mf_wfm_mainFrame_sbx_rletSclLst"
SEARCH_USAGE_LV3_INPUT_VALUES = ["대지", "염전"]
