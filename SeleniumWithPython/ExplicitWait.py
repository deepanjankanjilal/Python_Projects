from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://expedia.com")
#driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element(By.ID, "tab-flight-tab-hp").click()
time.sleep(2)
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/10/2018")

driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("15/10/2018")

#driver.find_element(By.XPATH, "//*[@id='search-button-hp-package']").click()

#driver.quit()



