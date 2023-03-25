# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 15:35:37 2020

@author: lockd

Whatsapp Automation Using Python

"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Opens Chrome
browser = webdriver.Chrome('D:\My Python Projects\Week11\Browser Automation\chromedriver')
browser.get('https://web.whatsapp.com/') #Opens Whatsapp
wait = WebDriverWait(browser, 600) #Sometimes net is slow, so this function will make program to wait for some time and not to get failed

#Name of friend to whom to send message
target = '"Shruti"' #Syntax '"Name"'
msg1 = "Hi Shruti" #Message to sent
msg2 = "What's up?"
msg3 = 'Aaaaaaaaoo'
msg4 = 'Wow!!!'


#Then Inspect to find the id of target message box. 
#body class -> div id -> div class -> span
#Here, span is given so find which span is of the target, 
#we will use following code
xArg = '//span[contains(@title,' + target + ')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, xArg)))
#wait.until(mrthod) calls the method until the return value is not False.
#EC.presence_of_element_located(locator) An expectation for checking that
#an element is present on the page. This does not necessarily mean 
#that the element is visible. locator - used to find the element and
#returns the WebElement once it is located
target.click()

#Now for sending message, I need to locate text box which can be done  
#by many ways. Here, we will be doing find by class
text_box = browser.find_element_by_class_name('DuUXI')

#Sending Message
text_box.send_keys(msg1+Keys.ENTER) #Enter because enter sends message in Whatsapp
#And Keys.Enter recognises that there should be an Enter key
text_box.send_keys(msg2+Keys.ENTER)
for i in range(50):
    text_box.send_keys(msg3+Keys.ENTER)
for i in range(50):
    text_box.send_keys(msg4+Keys.ENTER)
    
