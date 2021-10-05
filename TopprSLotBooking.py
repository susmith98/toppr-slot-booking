#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,WebDriverException
import time
import os


# In[4]:


driver=webdriver.Chrome(executable_path=os.path.join(r'E:\General','chromedriver.exe'))
#driver=webdriver.Firefox(executable_path=os.path.join(r'E:\General','geckodriver.exe'))


# In[3]:


## NAvigate to Toppr Login Page
driver.get('https://community.toppr.com/')


# In[35]:


## Finding and clicking on Login button
login_ele=driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div/div[1]/div[2]/button[1]')


# In[36]:


login_ele.click()


# In[37]:


email_ele=driver.find_element_by_id('email-login')


# In[38]:


pwd_ele=driver.find_element_by_id('password-login')


# In[39]:


email_ele.send_keys('<<Email>>')


# In[40]:


pwd_ele.send_keys('<<Password>>')


# In[41]:


login_ele=driver.find_element_by_xpath('//*[@id="login_modal_form"]/button[2]')


# In[42]:


login_ele.click()


# In[43]:


## Navigating to Slots page 
driver.get('https://community.toppr.com/doubts/slots/')


# In[13]:


l=driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]')


# In[14]:


L=l.find_elements_by_css_selector('*')


# In[19]:


L[9].click()


# In[57]:


last_ele=driver.find_element_by_xpath('//*[@id="2019-03-21"]')


# In[58]:


last_ele.click()


# In[59]:


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


# In[60]:


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


# In[3]:


## RUnning the script with the time gap of 5 seconds which would terminate when a slot is booked successfully
while True:
    isBooked = Book()
    if isBooked:
        break
    ## Wait for 5 seconds
    time.sleep(5)


# In[36]:


now = datetime.datetime.now()
print(now.minute)


# In[ ]:





# In[ ]:




