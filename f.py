#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:56:09 2020

@author: giri
"""

'''
Assert forgot password success message on the page http://the-internet.herokuapp.com/forgot_password
'''

from selenium import webdriver
from time import sleep

def main(usermailid):
    
    url = "http://the-internet.herokuapp.com/forgot_password"
    
    driver.get(url)
    
    sleep(1)
    
    driver.find_element_by_id('email').send_keys(usermailid)
    
    sleep(1)
    
    driver.find_element_by_id('form_submit').click()
    sleep(2)
    
    try :
        content = driver.find_element_by_id('content')
        
        if(content.text == "Your e-mail's been sent!"):
            print("successfully you have received mail from us , please check !!!")
            
        else:
            print("You might have entered wrong email id or you have not entered email id itself !!")
     
        driver.close()
    except :
        print("You have not entered email id or empty string entered from user")
        driver.close()


if __name__ == "__main__":
    usermailid = str(input("Provide your email id here to retrieve your password , \n like an example 1234@gmail.com : "))
    driver = webdriver.Chrome('./chromedriver')
    main(usermailid)
    