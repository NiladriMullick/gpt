import PyPDF2

def find_word_coordinates(input_pdf_path, word_to_find):
    # Open the PDF file
    with open(input_pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Get the first (and only) page
        page = pdf_reader.pages[0]

        # Get the text content of the page
        text_content = page.extract_text()

        # Find the word and its coordinates
        word_coordinates = []
        start_index = 0
        while True:
            start_index = text_content.find(word_to_find, start_index)
            if start_index == -1:
                break
            end_index = start_index + len(word_to_find)
            word_bbox = page.bbox_words()[start_index:end_index]
            word_coordinates.extend([(word['x0'], word['top'], word['x1'], word['bottom']) for word in word_bbox])
            start_index = end_index

        return word_coordinates

# Example usage:
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
word_to_find = 'your_word_here'  # Replace with the word you want to find

word_coordinates = find_word_coordinates(input_pdf_path, word_to_find)
if word_coordinates:
    for i, coordinates in enumerate(word_coordinates, 1):
        print(f"Instance {i}: Coordinates {coordinates}")
else:
    print(f"The word '{word_to_find}' was not found in the PDF.")
