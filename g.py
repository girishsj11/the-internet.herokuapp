#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 20:10:36 2020

@author: giri
"""

'''
Assert form validation functionality Post entering a dummy username and password on http://the-internet.herokuapp.com/login
'''

from selenium import webdriver
from time import sleep

def main(username,password):
    
    url = "http://the-internet.herokuapp.com/login"
    
    driver.get(url)
    
    sleep(2)
    
    driver.find_element_by_id('username').send_keys(username)
    
    driver.find_element_by_id('password').send_keys(password)
    
    driver.find_element_by_xpath('//*[@id="login"]/button').click()
    
    sleep(1)
    
    try : 
        
        if (driver.current_url == "http://the-internet.herokuapp.com/secure"):
            print("You Entered into secure area !!")
         
        elif(driver.current_url == url):
            print("You didnt entered valid username & password !!")
            
            
        driver.close()
        
    except :
        print("You have entered empty strings into username & password fields !!")

        



if __name__ == "__main__":
    
    username = "tomsmith"
    password = "SuperSecretPassword!"
    
    driver = webdriver.Chrome('./chromedriver')
    main(username,password)
    