import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

""" Program to perform context click or right mouse button click operation. """

# Create driver object
browser = webdriver.Chrome("C:\Tech_Made_Me_Lazy\Lib\Browser_Drivers\chromedriver.exe")

# Navigate to URL
browser.get("http://demo.guru99.com/test/simple_context_menu.html")

# Maximize the browser window
browser.maximize_window()

# Element to perform context click
right_click_element = browser.find_element_by_xpath("//span[text()='right click me']")

# Create actions object for performing Mouse and Keyword related activities
action_chains = ActionChains(browser)

# 1. Mouse to Element
# 2. Context Click or Right Mouse Button Click
action_chains.move_to_element(right_click_element).context_click(right_click_element).perform()

# Sleep for 5 Seconds
time.sleep(5)

# 1. Press Keyboard Down Arrow button
# 2. Press Keyboard Enter key button
action_chains.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

# Sleep for 5 Seconds
time.sleep(5)

# Quit the browser window
browser.quit()
