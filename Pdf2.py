import PyPDF2

def find_word_coordinates(input_pdf_path, word_to_find):
    # Open the PDF file
    with open(input_pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Get the first (and only) page
        page = pdf_reader.pages[0]

        # Iterate through each text element on the page
        for text_object in page.extract_words():
            text = text_object['text']
            if text == word_to_find:
                # Print the coordinates of the word
                x0, y0, x1, y1 = text_object['x0'], text_object['top'], text_object['x1'], text_object['bottom']
                print(f"Word '{word_to_find}' found at coordinates: ({x0}, {y0}, {x1}, {y1})")

# Example usage:
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
word_to_find = 'your_word_here'  # Replace with the word you want to find

find_word_coordinates(input_pdf_path, word_to_find)
