import time

from selenium import webdriver
from selenium.webdriver import ActionChains

""" Program to perform double click operation. """

# Create driver object
browser = webdriver.Chrome("C:\Tech_Made_Me_Lazy\Lib\Browser_Drivers\chromedriver.exe")

# Maximize the browser window
browser.maximize_window()

# Navigate to URL
browser.get("http://testautomationpractice.blogspot.com/")

# 'Field1' text box element for entering some data
field_1_element = browser.find_element_by_id('field1')

# 'Copy Text' button, when user double clicks this button, data is copied from 'Field1'
# text box to 'Field2' text box
copy_text_button = browser.find_element_by_xpath("//button[contains(text(),'Copy Text')]")

# clear 'Field1' text box before entering data
field_1_element.clear()

# Sleep for 5 Seconds
time.sleep(5)

# enter 'Hello Tech Made Me Lazy' data into 'Field1' text box
field_1_element.send_keys('Hello Tech Made Me Lazy')

# Sleep for 5 Seconds
time.sleep(5)

# create actions object for performing Mouse and Keyword related activities
action_chains = ActionChains(browser)

# perform double click operation on 'Copy Text' button
action_chains.double_click(copy_text_button).perform()

# Sleep for 5 Seconds
time.sleep(5)

# Quit the browser window
browser.quit()
