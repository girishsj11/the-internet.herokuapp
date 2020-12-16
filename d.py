#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:35:46 2020

@author: giri
"""
'''
Close the modal window and re-enable it on page http://the-internet.herokuapp.com/entry_ad

'''
from selenium import webdriver
from time import sleep

def entry_ad_close():
    element = driver.find_element_by_class_name('modal-footer')
    element.click()
    

def main():
    
    url = "http://the-internet.herokuapp.com/entry_ad"

    driver.get(url)
    
    sleep(3)
    
    #closing ad window 
    entry_ad_close()
    
    #re-enabling it again 
    driver.find_element_by_id("restart-ad").click()
    
    sleep(5)

if __name__ == "__main__":
    driver = webdriver.Chrome("./chromedriver")
    main()
    driver.close()