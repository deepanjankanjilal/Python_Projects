from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chromeOptions = Options()

chromeOptions.add_argument("download.default_directory = C:\DownloadedFiles")


chromeOptions.add_experimental_option("prefs",("download.default_directory", "C:\DownloadedFiles"))

driver = webdriver.Chrome(executable_path = "C:\Python3\Selenium_WebDriver\chromedriver\chromedriver.exe", chrome_options = chromeOptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

# Download Text File
driver.find_element_by_id("textbox").send_keys("testing download text file")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

# Download PDF File
driver.find_element_by_id("pdfbox").send_keys("testing pdf file")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()
