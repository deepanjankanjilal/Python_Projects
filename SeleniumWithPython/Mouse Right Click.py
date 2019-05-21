from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.maximize_window()

driver.get("http://demo.guru99.com/test/simple_context_menu.html")
btn = driver.find_element(By.XPATH, "//*[@id='authentication']/span")


actions = ActionChains(driver)
actions.context_click(btn).perform()
