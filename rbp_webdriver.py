'''
Created on Mar 24, 2017

@author: david
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

def rbp_webdriver():
    
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : "/Users/david/Documents/Home/Studium/Master/in-silico"} #set path for download here
    chromeOptions.add_experimental_option("prefs",prefs)

    driver = webdriver.Chrome('/Users/david/Documents/Home/Studium/Master/in-silico/selenium-3.3.1/chromedriver', chrome_options=chromeOptions)
    
    driver.get("http://cisbp-rna.ccbr.utoronto.ca/TFTools.php")
    assert "CISBP-RNA Database: Catalog of Inferred Sequence Binding Preferences of RNA binding proteins" in driver.title
    elem = driver.find_element_by_id("scanDNA")
    elem.clear()
    
    elem.send_keys("GCGCGCGGGCGCGC") #set sequence here
    
    element = driver.find_element_by_xpath("//select[@name='scanSpec']")
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        if option.get_attribute("value") == 'Mus_musculus': #set species here
            option.click()
            
    element = driver.find_element_by_xpath("//select[@name='whichScan']")
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        if option.get_attribute("value") == '3':
            option.click()
    
    
    
    
    element.submit()    
    assert "No results found." not in driver.page_source
    
    
    link = driver.find_element_by_link_text('Download excel spreadsheet (csv text format)')
    driver.get(link.get_attribute('href'))
    
    link_list = link.get_attribute('href').split('/')
    filename = link_list[-1]
    
    #change filename here 
    os.rename('/Users/david/Documents/Home/Studium/Master/in-silico/' + filename, '/Users/david/Documents/Home/Studium/Master/in-silico/example.csv') 

    driver.close()
    
#Tester

rbp_webdriver()