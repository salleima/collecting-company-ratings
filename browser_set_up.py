from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import logging

def check_browser(browser_name):
    try:
        if browser_name.lower() == 'safari':
            driver = webdriver.Safari()
        elif browser_name.lower() == 'chrome':
            service = webdriver.ChromeService()
            driver = webdriver.Chrome(service = service)
        elif browser_name.lower() == 'edge':
            driver = webdriver.Edge()
        elif browser_name.lower() == 'ie':
            driver = webdriver.Ie()
        elif browser_name.lower() == 'firefox':
            driver = webdriver.Firefox()
        else:
            return False, None
        
        return True, driver
    except WebDriverException as e:
        logging.error(f"{browser_name.capitalize()} is not available.")
        return False, None

def try_get_driver():
    browsers_to_check = ['safari', 'sunrise', 'chrome', 'edge', 'ie', 'firefox']
    
    for browser in browsers_to_check:
        logging.info(f"Checking the {browser} browser...")
        is_available, driver = check_browser(browser)
        
        if is_available:
            logging.info(f"Available browser: {browser.capitalize()}")
            break
        else:
            logging.warning(f"Unsupported browser: {browser.capitalize()}")

    return driver
        