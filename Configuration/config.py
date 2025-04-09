import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")
LINKEDIN_JOB_URL = os.getenv("JOB_URL")
CV_PATH = os.path.abspath(os.getenv("CV_PATH"))
WAIT_TIMEOUT = 30
SHORT_TIMEOUT = 5

ENTERPRISES = {
    "thales": {
        "url_keywords": ["thalesgroup.com", "thales"],
        "apply_button_selector": "button.btn-primary",
        "special_action": "navigate_to_thales_application_page",
        "new_tab": True,
    },
    "bpce": {
        "url_keywords": ["bpce"],
        "apply_button_selector": ".apply-btn",
        "special_action": "navigate_to_bpce_application_page",
    },
    "airbus": {
        "url_keywords": ["airbus"],
        "apply_button_selector": ".apply-button",
        "special_action": "navigate_to_airbus_application_page",
    },
    "orange": {
        "url_keywords": ["orange"],
        "apply_button_selector": "#detail-apply",
        "special_action": "navigate_to_orange_application_page",
    },
    "sopra-steria": {
        "url_keywords": ["soprasteria.com", "soprasteria", "smartrecruiters.com/SopraSteria1"],
        "special_action": "navigate_to_sopra_steria_application_page",
        "new_tab": True,
    }
}
