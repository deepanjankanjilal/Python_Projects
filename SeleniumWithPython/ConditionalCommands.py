from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")

driver.get("http://newtours.demoaut.com")
us_nm = driver.find_element_by_name("userName")

print(us_nm.is_displayed())
print(us_nm.is_enabled())

ps_wd = driver.find_element_by_name("password")
print(ps_wd.is_enabled())
print(ps_wd.is_displayed())

us_nm.send_keys("mercury")
ps_wd.send_keys("mercury")
driver.find_element_by_name("login").click()
rnd_trp_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
one_way_radio = driver.find_element_by_css_selector("input[value=oneway]")
print(rnd_trp_radio.is_selected())
print(one_way_radio.is_selected())



