from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")
driver.maximize_window()


driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-11").send_keys("C:/Users/kanjilad/Desktop/Img.bmp")
