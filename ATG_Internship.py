#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time

def test_case_1():
    browser.get('https://www.atg.party')
    time.sleep(5)
    login = browser.find_element_by_link_text('Login')
    login.click()
    time.sleep(1)
    email = browser.find_element_by_id('email')
    email.send_keys('hello@atg.world')
    password = browser.find_element_by_id('password')
    password.send_keys('Pass@123')
    sign = browser.find_element_by_class_name('btns-loger')
    sign.click()
    time.sleep(8)

def test_case_2():
    test_case_1()
    browser.get('https://www.atg.party/article')
    time.sleep(5)
    title = browser.find_element_by_id('title')
    title.send_keys('Final Test Case')
    desc = browser.find_element_by_class_name('fr-element.fr-view')
    desc.send_keys('This is my final test case.')
    time.sleep(2)
    post = browser.find_elements_by_id('featurebutton')
    post[-1].click()
    time.sleep(8)
    
   
options = webdriver.ChromeOptions()
options.headless = True
browser = webdriver.Chrome(chrome_options = options)
test_case_2()
print("Code executed successfully. Output sent")  


# In[ ]:




