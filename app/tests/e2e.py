from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import ChromiumOptions
import sys


def test_scores_service(app_url):
       
    print("Here goes nothing!!")

    chrome_options = ChromiumOptions()
    service = Service(ChromeDriverManager().install(), options=chrome_options)

    driver = webdriver.Chrome(service=service)

    driver.get("http://localhost:8777/")
    score_element = driver.find_element(By.ID,"score")
    if not score_element:
        print("no score element found")
        return '-1'
    test_result = score_element.text
    print("test result is " + test_result)
    if not test_result:
       print("no test result found")
       return '-1'
    return test_result

def main_function():
    app_url = "http://localhost:8777/"
    test_result = test_scores_service(app_url)
    print(test_result)
    int_test_result = int(test_result)
    print(int_test_result)
    if(int_test_result > 1000 or int_test_result < 1):
       return sys.exit(-1)
    return sys.exit(0)



main_function()

