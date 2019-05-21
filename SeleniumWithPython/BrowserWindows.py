from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)
all_wind = driver.window_handles
print(all_wind)
for handle in all_wind:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()
driver.quit()
driver.save_screenshot('screen.png')
driver.get_screenshot_as_png()
driver.get_screenshot_as_file('screen1.png')



