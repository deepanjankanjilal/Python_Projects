from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.implicitly_wait(5)

driver.get("http://newtours.demoaut.com")
time.sleep(5)
driver.maximize_window()

# Number pf links
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

# Print all the links
for link in links:
    print(link.text)

# Click on a link
driver.find_element(By.LINK_TEXT, "REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "SUP").click()
