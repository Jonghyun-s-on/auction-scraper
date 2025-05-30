from selenium.webdriver.common.by import By

FORM_SELECTOR = {
    "submit_button": {
        "type": "button",
        "by": By.ID,
        "value": "mf_wfm_mainFrame_btn_gdsDtlSrch",
    },
    "court_input": {
        "type": "select",
        "by": By.ID,
        "value": "mf_wfm_mainFrame_sbx_rletCortOfc",
    },
    "bid_type_input": {
        "type": "radio",
        "by": By.CSS_SELECTOR,
        "options": {
            "기일입찰": "label[for='mf_wfm_mainFrame_rad_mvprpBidLst_input_0']",
            "기간입찰": "label[for='mf_wfm_mainFrame_rad_mvprpBidLst_input_1']",
            "전체": "label[for='mf_wfm_mainFrame_rad_mvprpBidLst_input_2']",
        },
    },
    "start_date_input": {
        "type": "text",
        "by": By.ID,
        "value": "mf_wfm_mainFrame_cal_rletPerdStr_input",
    },
    "end_date_input": {
        "type": "text",
        "by": By.ID,
        "value": "mf_wfm_mainFrame_cal_rletPerdEnd_input",
    },
    "usage_lv1_input": {
        "type": "select",
        "by": By.ID,
        "value": "mf_wfm_mainFrame_sbx_rletLclLst",
    },
    "usage_lv2_input": {
        "type": "select",
        "by": By.ID,
        "value": "mf_wfm_mainFrame_sbx_rletMclLst",
    },
    "usage_lv3_input": {
        "type": "select",
        "by": By.ID,
        "value": "mf_wfm_mainFrame_sbx_rletSclLst",
    },
}

RESULT_SELECTOR = {
    "page_size_input": {
        "type": "select",
        "by": By.ID,
        "value": "mf_wfm_mainFrame_sbx_pageSize"
    },
    "content_box": {
        "type": "container",
        "by": By.ID,
        "value": "mf_wfm_mainFrame_grp_contests",
    },
    "next_page_button": {
        "type": "button",
        "by": By.ID,
        "value": "mf_wfm_mainFrame_pgl_gdsDtlSrchPage_next_btn",
    },
}
