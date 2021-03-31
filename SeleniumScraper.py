# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from requests import get
import chromedriver_binary
import time

#Time the event 
starttime = time.time() 

txt1 = None
txt = None 


while True:
    
    #locate Chrome Driver
    driver = webdriver.Chrome('C:\Program Files\Python38\chromedriver.exe')
    #Go to the url
    driver.get("https://www.sec.gov/cgi-bin/browse-edgar?company=&CIK=&type=8-K&owner=include&count=40&action=getcurrent")
    
    print("Opening New Browser")
    
    PostVal = driver.find_element_by_xpath("//tr[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//td[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]")
    txt = PostVal.text 
  
    #if its the same as the last dont do anything 
    if txt != txt1:
        print(driver.title)
        
        #select first element available
        elem = driver.find_element_by_xpath("/html/body/div/table[2]/tbody/tr[3]/td[2]/a[1]")
        #click element in 22
        elem.click()
        
        url = driver.current_url
        driver.get(url)
        XBelem = driver.find_element_by_xpath(".//tr[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//a")
        XBelem.click()
        time.sleep(20.0 - ((time.time() - starttime) % 20.0))
        driver.quit() 
        
        print("Browser Closed")
        
        
    else:
        
        driver.quit()
        
        print("Values are the same closing browser")
        
 