#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:06:42 2020

@author: giri
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


def main():
    #getting the webpage link to url variable
    url = "http://the-internet.herokuapp.com/dropdown"
    
    #loading Chrome driver onto the webdriver package
    driver = webdriver.Chrome("./chromedriver")
    
    #loading the url variable onto the driver of chrome
    driver.get(url)
    
    #selecting & finding out only id's named with dropdown
    element = driver.find_element_by_id("dropdown")
    
    #getting listout of all optons by Select class
    dropdown_options = Select(element)
    
    for _ in dropdown_options.options:
        print(_.text)
        
    
    #selecting one of the option 2 set among the all options   
    dropdown_options.select_by_value("2") 
    print("\n Selected Option 2 !")
     
    sleep(3)
    driver.close()

if __name__ == "__main__":
    main()