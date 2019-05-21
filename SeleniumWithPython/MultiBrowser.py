from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
#driver = webdriver.Firefox(executable_path = "C:\Python3\Selenium_WebDriver\geckodriver-v0.24.0-win64\geckodriver.exe")
#driver = webdriver.Ie(executable_path = "C:\Python3\Selenium_WebDriver\IEDriverServer_x64_3.14.0\IEDriverServer.exe")
driver.get("http://newtours.demoaut.com")

print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()
driver.quit()
