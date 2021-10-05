#!/usr/bin/env python
# coding: utf-8

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,WebDriverException
import time
import os

## Loading the chrome driver
driver=webdriver.Chrome(executable_path=os.path.join(r'E:\General','chromedriver.exe'))

## NAvigate to Toppr Login Page
driver.get('https://community.toppr.com/')

## Finding and clicking on Login button
login_ele=driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[1]/div[2]/button[1]')

login_ele.click()

email_ele=driver.find_element_by_id('email-login')

pwd_ele=driver.find_element_by_id('password-login')

email_ele.send_keys('<<Email>>')

pwd_ele.send_keys('<<Password>>')

login_ele=driver.find_element_by_xpath('//*[@id="login_modal_form"]/button[2]')

login_ele.click()

## Navigating to Slots page 
driver.get('https://community.toppr.com/doubts/slots/')

## Storing the selectors of each time slot element on screen i.e 3pm, 4pm, 5pm....
## Included only 3-7PM slots selector is because, I'm only interested to book those slots
Three='//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[4]/div'
Four='//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[5]/div'
Five='//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[6]/div'
Six='//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[7]/div'
Seven='//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[8]/div'
Sixpm='//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div/div[3]/div'
Sevenpm='//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div/div[4]/div'
Slots=[Three,Four,Five,Six,Seven,Sixpm,Sevenpm]

def Book():
    for i in Slots:
        e=driver.find_element_by_xpath(i)
        try:
            e.click()
        except WebDriverException:
            continue
        try:
            ## If Confirm Book slot button is available -> click it to confirm the booking
            book=driver.find_element_by_css_selector('body > div.ReactModalPortal > div > div > div._176vP > div._2gOMG > button.wGytW.sc-htpNat.cPKwvO')
            book.click()
            time.sleep(0.3)
            return True
        except NoSuchElementException: 
            ## If SLot is not available -> a pop up message is displayed with got it button
            ## When Got it button is clicked, pop up is closed and we can click on other slot buttons
            gotit=driver.find_element_by_css_selector('body > div.ReactModalPortal > div > div > button')
            gotit.click()
            time.sleep(0.3)
        return False


## RUnning the script with the time gap of 5 seconds which would terminate when a slot is booked successfully
while True:
    isBooked = Book()
    if isBooked:
        break
    ## Wait for 5 seconds
    time.sleep(5)



