import time

from selenium import webdriver
from selenium.webdriver import ActionChains

""" Program to perform Mouse Hover operation. """

# Create driver object
browser = webdriver.Chrome("C:\Tech_Made_Me_Lazy\Lib\Browser_Drivers\chromedriver.exe")

# Maximize the browser window
browser.maximize_window()

# Navigate to URL
browser.get("http://demowebshop.tricentis.com/")

# 'COMPUTERS' menu button for performing Mouse Hover operation.
computers_menu = browser.find_element_by_partial_link_text('COMPUTERS')

# 'ELECTRONICS' menu button for performing Mouse Hover operation.
electronics_menu = browser.find_element_by_partial_link_text('ELECTRONICS')

# create actions object for performing Mouse and Keyword related activities
action_chains = ActionChains(browser)

# perform Mouse Hover operation on 'COMPUTERS' menu button
action_chains.move_to_element(computers_menu).perform()

# Sleep for 5 Seconds
time.sleep(5)

# perform Mouse Hover operation on 'ELECTRONICS' menu button
action_chains.move_to_element(electronics_menu).perform()

# Sleep for 5 Seconds
time.sleep(5)

# Quit the browser window
browser.quit()