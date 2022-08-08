from tkinter import X
import undetected_chromedriver as uc
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os, random, time, requests
from multiprocessing import Pool
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd

cwd = os.getcwd()
opts = uc.ChromeOptions()

 
opts.headless = False
 
 
opts.add_argument("--disable-popup-blocking")
 
 
 
def xpath_type(el,mount):
    sleep(3)
    return wait(browser,15).until(EC.element_to_be_clickable((By.XPATH, el))).send_keys(mount)
 
         
def xpath_el(el):
    element_all = wait(browser,30).until(EC.element_to_be_clickable((By.XPATH, el)))
    
    return browser.execute_script("arguments[0].click();", element_all)
 
    
def subs(data):
    
    try:
        email = input_email.split("@")[0]+str(data)+"@"+input_email.split("@")[1]
        password = input_password
        global browser
        opts = uc.ChromeOptions()

 
        opts.headless = False
        
        
        opts.add_argument("--disable-popup-blocking")
        browser = uc.Chrome(options=opts,driver_executable_path=f"{cwd}//chromedriver.exe")
        browser.get(input_link)
        browser.get(wait(browser,15).until(EC.presence_of_element_located((By.XPATH, f'//a[contains(@href,"https://accounts.google.com/ServiceLogin?")]'))).get_attribute("href"))

        xpath_type('//input[@type="email"]',email)
        xpath_type('//input[@type="email"]',Keys.ENTER)
        xpath_type('//input[@type="password"]',password)
        xpath_type('//input[@type="password"]',Keys.ENTER)
        try:
            wait(browser,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#accept"))).click()
        except:
            pass
        sleep(8)
        browser.get(input_link)
        sleep(1)
        browser.get(input_link)
        xpath_el('//tp-yt-paper-button[@class="style-scope ytd-subscribe-button-renderer"]')
        sleep(3)
        notifier = wait(browser,3).until(EC.presence_of_element_located((By.XPATH, f'//yt-formatted-string[@class="style-scope ytd-subscribe-button-renderer"]'))).text
        print(f"[{time.strftime('%d-%m-%y %X')}] [{email}] {notifier}")
        sleep(5)
        browser.quit()
    except Exception as e:
 
        try:
            browser.quit()
        except:
            pass
    
if __name__ == '__main__':
    global input_link
    global input_email
    global input_password
    print("[*] Automation Subs YT")
    input_link = input("[*] Input URL: ")
    input_email = input("[*] Input Email: ")
    input_password = input("[*] Input Password: ")
    start = int(input("[*] Start From: "))
    check_much = input("[*] End to: ")
    total =  [x for x in range(start,int(check_much))]
    start = time.time()
   
    for i in total: 
        
        subs(i)
            
    end = time.time()
    print("[*] Time elapsed: ", end - start)
