from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)

# Click on Ok button in alert
#driver.switch_to.alert.accept()

# Click on Cancel button in alert
driver.switch_to.alert.dismiss()

