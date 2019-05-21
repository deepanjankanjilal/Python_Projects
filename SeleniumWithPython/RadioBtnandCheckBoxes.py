from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.implicitly_wait(5)

driver.get("http://www.practiceselenium.com/practice-form.html")
time.sleep(5)

# Get the status of Male radio button
sts_dis = driver.find_element(By.ID, "sex-0").is_displayed()
sts_enb = driver.find_element(By.ID, "sex-0").is_enabled()
sts_sel = driver.find_element(By.ID, "sex-0").is_selected()
print(sts_dis, sts_enb, sts_sel)

# Get the status of Female radio button
sts_dis = driver.find_element(By.ID, "sex-1").is_displayed()
sts_enb = driver.find_element(By.ID, "sex-1").is_enabled()
sts_sel = driver.find_element(By.ID, "sex-1").is_selected()
print(sts_dis, sts_enb, sts_sel)

# Click on Female radio button
driver.find_element(By.ID, "sex-1").click()

# Again print the selected status
fsts_sel = driver.find_element(By.ID, "sex-1").is_selected()
msts_sel = driver.find_element(By.ID, "sex-0").is_selected()
print(fsts_sel, msts_sel)

# Working with check boxes
# Get the status of Male radio button
sts_dis = driver.find_element(By.ID, "exp-0").is_displayed()
sts_enb = driver.find_element(By.ID, "exp-0").is_enabled()
sts_sel = driver.find_element(By.ID, "exp-0").is_selected()
print(sts_dis, sts_enb, sts_sel)

# Click on 2 check box
driver.find_element(By.ID, "exp-1").click()

# Again print the selected status
fsts_sel = driver.find_element(By.ID, "exp-1").is_selected()
msts_sel = driver.find_element(By.ID, "exp-0").is_selected()
print(fsts_sel, msts_sel)
