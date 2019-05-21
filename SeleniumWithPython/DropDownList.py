from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.implicitly_wait(5)

driver.get("http://www.practiceselenium.com/practice-form.html")
time.sleep(5)
ele = (driver.find_element(By.ID, "continents"))
drp = Select(ele)

# Select by visible text
drp.select_by_visible_text('Europe')

# Select by index
drp.select_by_index(2)

# Select by value
#drp.deselect_by_value('')

# Capture all the available options
opt = drp.options
for count in opt:
    print(count.text)

# Count the number of options
print(len(drp.options))