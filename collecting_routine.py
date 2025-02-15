from browser_set_up import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv

def collecting_routine():
    driver = try_get_driver()
    
    if driver == None:
        logging.critical(f"All browsers are unavailable.")
        return
    
    with open('data-samples/vacancies.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        links_list = []
        for row in reader:
            formatted_row = ''.join(row)
            links_list.append(formatted_row)
    
    for link in links_list:
        driver.get(link)
        try:
            company_element = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span.vacancy-company-name span.magritte-text___pbpft_3-0-27 span"))
            )
            
            company_title = company_element.text
            if not company_title:
                company_title = company_element.get_attribute('textContent')
            logging.info(f"The company's title \"{company_title}\" was received correctly.")
        except TimeoutException:
            logging.warning(f"The company's title is not on the page.")
            company_title = "n/a"
        
        try:
            rating_element = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.ZTc9YHr___content-rating div[data-qa='employer-review-small-widget-total-rating']"))
            )
            
            rating_number = rating_element.text
            if not rating_number:
                rating_number = rating_element.get_attribute('textContent')
                
            logging.info(f"The company's rating \"{rating_number}\" was received correctly.")
        except TimeoutException:
            logging.warning(f"The company's rating is not on the page.")
            rating_number = "n/a"
        
        print(f"Company: {company_title}. Rating: {rating_number}")

    driver.quit()
