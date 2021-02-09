from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time
from paths import driverPath

chrome_options=Options()
driver = webdriver.Chrome(driverPath,chrome_options=chrome_options)

def pick_all(url,xpaths,wait=10):
    driver.get(url)
    data=[]
    for key,xpath in xpaths.items():
        try:
            element=WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH,xpath)))
            data.append(element.get_attribute('href')) if(key.startswith('#')) else data.append(element.text)
        except:
            data.append("None") 
    return data

def pick(xpath,url,wait=10):
    driver.get(url)
    try:
        return WebDriverWait(driver, wait).until(EC.presence_of_element_located((By.XPATH,xpath))).text
    except:
        return "None"  

def pick_similar(xpath,attribute,url,wait=10):
    driver.get(url)
    try: 
        elements = WebDriverWait(driver, wait).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
    except:
        return "None"
    data=[]
    for element in elements:
        data.append(element.get_attribute(attribute))
    return data


def pick_group(parent_xpath,want_text,url):
    driver.get(url)
    children=parent.find_elements(By.XPATH,"./child::*")
    return data

def get_children(parent,want_text=False):
    children=parent.find_elements(By.XPATH,"./child::*")
    return  [i.text for i in children]







