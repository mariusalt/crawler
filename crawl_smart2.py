from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback
import sys
import csv

inp = open('guestFile2.csv', 'rt', encoding='utf8')
outFile = open('out-battery.csv', 'wt', encoding='utf8')
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe", chrome_options=chrome_options)
bat=[]
nam=[]
comp=[]
telo=[]
for iter, row in enumerate(inp):
    tel = row.split(";")
    print(', '.join(tel))
    print("loading url into browser... %s" % tel[0])
    try:
        driver.get('https://www.phonearena.com/')
        time.sleep(4)
        #fld2 = driver.find_element_by_class_name("fc-button.fc-button-consent")
    #    element = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[2]/section[1]/div[3]/button[1]")))

     #   element.click();
       
       # fdl2 = driver.find_element_by_link_text("I ACCEPT")
        #fld2 = driver.find_element_by_class_name(xpath)
       # fld2=driver.find_element_by_css_selector("[role=button]")
      #  fld2.click()
       # time.sleep(3)
        if "noticed some unusual activity coming from your computer network" in driver.page_source:
            print("CAPTCHA encountered")
            quit()
      #  suchfeld = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="form-control"]')))
        suchfeld=driver.find_element_by_xpath("/html/body/div[1]/header/nav[2]/div/div[1]/div[2]/div[2]/div/form/div/input")
        suchfeld.clear()
      #  suchfeld.send_keys(tel[0])
        suchfeld.send_keys(tel[0])
        time.sleep(1)
        suchfeld.send_keys('\n')
        time.sleep(3)
        link=driver.find_element_by_xpath('//*[@id="search-phones"]/div[3]/div[1]/div/a')
        ref=link.get_attribute("href")
        print(ref)
        driver.get(ref)
        time.sleep(2)
      #  b=[]
        battery=driver.find_element_by_xpath('//*[@id="phones-content-inner"]/div/div/div/div[1]/article/div/section[1]/div/aside/ul[1]/li[6]/span[2]').text
        print(battery)
        bat.append(battery)        
    #    print(b)
        for n,l in enumerate(bat):
            s = str(l)
            s = s[:4]
            bat[n]=s
       # print(b)
       # bat.append(b)
        name=driver.find_element_by_xpath('//*[@id="phones-content-inner"]/div/div/div/div[1]/article/div/section[1]/div/header/div[1]/div/div[1]/h1').text
        print(name)
    #    m=[]
     #   m.append(name)
        nam.append(name)

        telo.append(tel[0])

        if name==tel[0]:
            comp.append('same')
        else:
            comp.append('diff')

        with open('battery.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['TelHom','Battery','TelList','Match'])
            writer.writerows(zip(nam,bat,telo,comp))

     #       browser.get(landtag[1])
    #        time.sleep(2)
     #       if "noticed some unusual activity coming from your computer network" in browser.page_source:
      #          print("CAPTCHA encountered")
       #         sendEmail("selenium failure: captcha",
        #    "captcha", "buchmann@zew.de")
     #           quit()
      #      # Search for single element
       #     direkt = browser.find_element_by_xpath(
        #    "//table[@class='ohne-rand m-u-0']//td//a").get_attribute('href')
         #   print(direkt)
    except Exception as e:
        print("\nException in inner loop:\n")
        print(traceback.format_exc())

print("loop end")

driver.quit()
