from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.maximize_window()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
src = driver.find_element(By.XPATH, "//*[@id='box7']")
dst = driver.find_element(By.XPATH, "//*[@id='box107']")


actions = ActionChains(driver)

actions.drag_and_drop(src, dst).perform()