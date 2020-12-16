#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:37:33 2020

@author: giri
"""

'''
Write a test to enter alphabets on this and mark it as a failure if we cannot enter on page http://the-internet.herokuapp.com/inputs

'''

from selenium import webdriver
from time import sleep

def main(key):
    
    url = "http://the-internet.herokuapp.com/inputs"
    
    driver.get(url)
    
    sleep(2)

    element = driver.find_element_by_xpath('//input[@type="number"]')

    element.send_keys(key)
    
    get_value = element.get_attribute('value')

    if(len(get_value)==0):
        print("Failure on entering the alphabets !")
    else:
        print("Entered succesfully !")

    sleep(2)
        
    driver.close()
    

if __name__ == "__main__":
    
    key = str(input("Enter your favourite alphabet to check on webpage : "))
    
    driver = webdriver.Chrome("./chromedriver")
    
    main(key)
    
 
    
    
    
    