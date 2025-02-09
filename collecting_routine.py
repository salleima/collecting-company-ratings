from selenium import webdriver
from browser_set_up import *

def collecting_routine():
    # Trying to open the browser driver
    driver = try_get_driver()
    
    if driver == None:
        print(f"All browsers are unavailable.") # TODO: add logging
        return
    
    driver.quit()
