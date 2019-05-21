from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# Scroll down the page by pixel
driver.execute_script("window.scrollBy(0,2000)","")

# Scroll down the page till element found
flg = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();",flg)

# Scroll to the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

