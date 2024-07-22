from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import ChromiumOptions

print("Here goes nothing!!!!!!!!")

chrome_options = ChromiumOptions()
service = Service(ChromeDriverManager().install(), options=chrome_options)

driver = webdriver.Chrome(service=service)

driver.get("http://localhost:8777/")



test_result = driver.find_element(By.ID,"score").text
print(test_result)
assert test_result > "1"
