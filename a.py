#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:07:20 2020

@author: giri
"""
'''
Assert Broken images http://the-internet.herokuapp.com/broken_images
'''



from selenium import webdriver
from time import sleep


def main():
    #getting the webpage link to url variable
    url = "http://the-internet.herokuapp.com/broken_images"
    
    #loading Chrome driver onto the webdriver package
    driver = webdriver.Chrome('./chromedriver')
    
    #loading the url variable onto the driver of chrome
    driver.get(url)
    sleep(5)
    
    element = driver.find_elements_by_css_selector('img')
    
    for each in element:
        try:
            if(each.get_attribute('naturalWidth')=='0'):
                print("Broken image : ",each.get_attribute('outerHTML'))
            else:
                print()
                print("Proper image : ",each.get_attribute('outerHTML'))
        
        except:
            print("Nothing to catch here !")
    
    driver.close()


if __name__ == "__main__":
    main()
        

