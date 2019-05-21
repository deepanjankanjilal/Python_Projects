from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.implicitly_wait(5)

driver.get("https://www.formsite.com/templates/registration-form-templates/race-registration-form/")
time.sleep(5)

# Count the nu,ber of input boxes present
inp_boxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(inp_boxes))

# Enter values into input boxes
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("deep")

# Get the status
sts_dis = driver.find_element(By.ID, "RESULT_TextField-2").is_displayed()
sts_enb = driver.find_element(By.ID, "RESULT_TextField-2").is_enabled()
print(sts_dis)
print(sts_enb)

