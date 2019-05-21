from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element(By.XPATH, "//*[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH, "//*[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH, "//*[@id='btnLogin']").click()
adm = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']/b")
usr_mg = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
usr = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")


actions = ActionChains(driver)
actions.move_to_element(adm).move_to_element(usr_mg).move_to_element(usr).click().perform()
