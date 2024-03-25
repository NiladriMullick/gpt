import fitz  # PyMuPDF
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to your Chrome WebDriver executable
chrome_driver_path = 'path_to_chrome_driver'

# Path to your PDF file
pdf_file_path = 'path_to_pdf_file'

# Word to search and highlight
word_to_search = 'your_word'

# Start a Chrome WebDriver session
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the PDF file
doc = fitz.open(pdf_file_path)

# Iterate through each page to search for the word and highlight it
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text_instances = page.search_for(word_to_search)

    for inst in text_instances:
        # Get the coordinates of the text instance
        left = inst[0]
        bottom = page.rect.height - inst[1]  # Flip y-coordinate
        right = inst[2]
        top = page.rect.height - inst[3]  # Flip y-coordinate

        # Draw a rectangle around the text instance (highlighting)
        page.add_rect(fitz.Rect(left, bottom, right, top), color=(1, 1, 0))

# Save the modified PDF with highlighted text
highlighted_pdf_path = 'highlighted_pdf.pdf'
doc.save(highlighted_pdf_path)

# Close the PDF document
doc.close()

# Open the modified PDF in Chrome and take a screenshot
driver.get(f'file://{highlighted_pdf_path}')
driver.save_screenshot('highlighted_pdf_screenshot.png')

# Close the WebDriver session
driver.quit()
