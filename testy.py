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

bat=[['1004 mAh'],['3492jfkdsjo'],['100hfdjsknfkj']]

for n,l in enumerate(bat):
            for val in l:
                s = str(val)
                s = s[:4]
                bat[n]=s
print(bat)
