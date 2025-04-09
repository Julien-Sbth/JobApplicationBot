from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from Configuration.config import WAIT_TIMEOUT, SHORT_TIMEOUT
def initialize_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-webrtc")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-extensions")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(SHORT_TIMEOUT)
    return driver, WebDriverWait(driver, WAIT_TIMEOUT)
