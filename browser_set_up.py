from selenium import webdriver
from selenium.common.exceptions import WebDriverException

def check_browser(browser_name):
    try:
        if browser_name.lower() == 'safari':
            driver = webdriver.Safari()
            print(f"Available browser: {browser_name}") # TODO: add logging
        elif browser_name.lower() == 'chrome':
            driver = webdriver.Chrome()
            print(f"Available browser: {browser_name}") # TODO: add logging
        elif browser_name.lower() == 'edge':
            driver = webdriver.Edge()
            print(f"Available browser: {browser_name}") # TODO: add logging
        elif browser_name.lower() == 'ie':
            driver = webdriver.Ie()
            print(f"Available browser: {browser_name}") # TODO: add logging
        elif browser_name.lower() == 'firefox':
            driver = webdriver.Firefox()
            print(f"Available browser: {browser_name}") # TODO: add logging
        else:
            print(f"Unsupported browser: {browser_name}") # TODO: add logging
            return False, None
        
        return True, driver
    except WebDriverException as e:
        print(f"{browser_name.capitalize()} is not available: {e}")
        return False, None

def try_get_driver():
    browsers_to_check = ['safari', 'chrome', 'edge', 'ie', 'firefox']
    
    for browser in browsers_to_check:
        is_available, driver = check_browser(browser)
        if is_available:
            break

    return driver
        