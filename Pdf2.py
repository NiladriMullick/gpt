from pdfminer.high_level import extract_text
from pdfminer.layout import LTTextContainer

def find_word_coordinates(input_pdf_path, word_to_find):
    # Extract text content from the PDF
    text = extract_text(input_pdf_path)

    # Iterate through each text object
    for text_container in extract_text(input_pdf_path, laparams=None):
        if isinstance(text_container, LTTextContainer):
            for text_line in text_container:
                # Check if the word is present in the text line
                if word_to_find in text_line.get_text():
                    # Get the coordinates of the text line
                    x0, y0, x1, y1 = text_line.bbox
                    print(f"Word '{word_to_find}' found at coordinates: ({x0}, {y0}, {x1}, {y1})")

# Example usage:
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
word_to_find = 'your_word_here'  # Replace with the word you want to find

find_word_coordinates(input_pdf_path, word_to_find)
