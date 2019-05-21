from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
ele = driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")


actions = ActionChains(driver)
actions.double_click(ele).perform()
