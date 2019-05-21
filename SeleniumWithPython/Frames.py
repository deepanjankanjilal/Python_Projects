from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.maximize_window()

driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
driver.switch_to.frame("packageListFrame") # first frame
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
time.sleep(10)

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame") # second frame
driver.find_element(By.LINK_TEXT, "WebDriver").click()
time.sleep(10)
driver.switch_to.default_content()

driver.switch_to.frame("classFrame") # third frame
driver.find_element(By.XPATH, "/html/body/div[1]/ul/li[5]").click()
time.sleep(10)


