from browser_set_up import *

def collecting_routine():
    # Trying to open the browser driver
    driver = try_get_driver()
    
    if driver == None:
        logging.critical(f"All browsers are unavailable.")
        return
    
    links = ["https://nn.hh.ru/vacancy/116171255?query=Python+developer&hhtmFrom=vacancy_search_list"]
    
    for link in links:
        driver.get(link)
        title = driver.title
        print(title)

    
    driver.quit()
