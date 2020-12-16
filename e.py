#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 19:37:08 2020

@author: giri
"""

'''
Assert file upload functionality on http://the-internet.herokuapp.com/upload for PNG images.
'''
import os
from selenium import webdriver
from time import sleep


def main():
    url = "http://the-internet.herokuapp.com/upload"
    
    driver.get(url)
    
    sleep(2)
    #clicking button where we need to select png file & we need to make sure from local computer it will selects only png file
    driver.find_element_by_id('file-upload').send_keys(os.getcwd()+"/world.png")
    
    sleep(2)
    #clicking submit/upload button 
    driver.find_element_by_id('file-submit').click()
    
    sleep(2)
    
    

if __name__ == "__main__":
    driver = webdriver.Chrome('./chromedriver')
    main()
    driver.close()