from selenium import webdriver
driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")

driver.get("http://newtours.demoaut.com/mercurywelcome.php")

driver.save_screenshot("C:\Screenshots\homepage.png")
driver.get_screenshot_as_file("C:\Screenshots\homepage2.png")