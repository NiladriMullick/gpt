from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Path to your Chrome WebDriver executable
chrome_driver_path = 'path_to_chrome_driver'

# Path to your PDF file
pdf_file_path = 'path_to_pdf_file'

# Word to search
word_to_search = 'your_word'

# Start a Chrome WebDriver session
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the PDF file in Chrome
driver.get(f'file://{pdf_file_path}')

# Wait for the PDF to load
time.sleep(2)  # Adjust this as needed

# Simulate pressing Ctrl+F to bring up the find dialog
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'f')

# Find the search input field and enter the word to search
search_input = driver.switch_to.active_element
search_input.send_keys(word_to_search)

# Wait for a while to let the search results appear
time.sleep(2)  # Adjust this as needed

# Take a screenshot
driver.save_screenshot('pdf_search_result.png')

# Close the WebDriver session
driver.quit()
