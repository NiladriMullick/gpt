from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your Chrome WebDriver executable
chrome_driver_path = 'path_to_chrome_driver'

# Path to your PDF file
pdf_file_path = 'path_to_pdf_file'

# Word to search and highlight
word_to_search = 'your_word'

# Start a Chrome WebDriver session
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the PDF file in Chrome
driver.get(f'file://{pdf_file_path}')

# Wait for the PDF to load
time.sleep(2)  # Adjust this as needed

# Execute JavaScript to search and highlight the word
driver.execute_script(f'''
    var searchTerm = "{word_to_search}";
    var pdfViewer = document.querySelector("embed[type='application/pdf']");
    var pdfWindow = pdfViewer.getSVGWindow();
    var pdfDocument = pdfWindow.document;
    var textLayer = pdfDocument.querySelector(".textLayer");

    function findAndHighlight(searchTerm) {{
        var textDivs = textLayer.querySelectorAll("div");
        textDivs.forEach(function(div) {{
            if (div.textContent.includes(searchTerm)) {{
                var text = div.textContent;
                var index = text.indexOf(searchTerm);
                var modifiedText = "<span style='background-color: yellow'>" + text.substr(index, searchTerm.length) + "</span>";
                div.innerHTML = text.substr(0, index) + modifiedText + text.substr(index + searchTerm.length);
            }}
        }});
    }}

    findAndHighlight(searchTerm);
''')

# Take a screenshot
driver.save_screenshot('highlighted_pdf.png')

# Close the WebDriver session
driver.quit()
