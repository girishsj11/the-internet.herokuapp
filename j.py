#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:25:41 2020

@author: giri
"""

'''
Right a looped script to assert a 'successful notification" after repeated unsuccessful notification on page http://the-internet.herokuapp.com/notification_message_rendered
'''

from selenium import webdriver
from time import sleep


def click():
    
    driver.find_element_by_xpath('//*[@id="content"]/div/p/a').click()
    sleep(1)
    
def main():
    url = "http://the-internet.herokuapp.com/notification_message_rendered"
    
    driver.get(url)
    
    sleep(2)

    click()
    element = driver.find_element_by_id("flash")
    
    if((element.text).count('successful') >=1):
            print("Action is successfull & webpage will close soon")
            sleep(3)
            driver.close()
    else:
        while((element.text).count('Action unsuccesful') >=1):
            click()
            
            if((element.text).count('Action successful') >=1):
                print("Action is successfull & webpage will close soon")
                sleep(3)
                driver.close()
                
            else:
                continue


if __name__ == "__main__":
    driver = webdriver.Chrome('./chromedriver')
    main()
    