#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:21:23 2020

@author: giri
"""

'''
Select 'option 2' from the drop-down http://the-internet.herokuapp.com/dropdown

'''


from selenium import webdriver
from time import sleep


def main():
    
    url = "http://the-internet.herokuapp.com/dynamic_loading/1"
    
    driver = webdriver.Chrome("./chromedriver")
    
    driver.get(url)
    
    sleep(5)
    
    start_button = driver.find_element_by_xpath('//*[@id="start"]/button')
    
    start_button.click()
    
    sleep(5)
    
    finish_button = driver.find_element_by_id("finish").text
    
    if(finish_button=='Hello World!'):
        sleep(2)
        print("Sucessfully page loaded & finished !! ")
        
    else:
        print("still webpage is loading !!!")
    
    driver.close()
    
if __name__ == "__main__":
    main()
    
    