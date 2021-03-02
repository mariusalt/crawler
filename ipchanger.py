from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import traceback

chrome_options = webdriver.ChromeOptions()


driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe", chrome_options=chrome_options)
driver.get('https://www.wieistmeineip.de/')
time.sleep(5)
driver.quit()

