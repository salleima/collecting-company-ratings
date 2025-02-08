from selenium import webdriver

def collecting_routine():
    driver = webdriver.Chrome()

    driver.get("https://nn.hh.ru/vacancy/116171255?query=Python+developer&hhtmFrom=vacancy_search_list")

    title = driver.title

    driver.implicitly_wait(0.5)

    print(title)
    driver.quit()
