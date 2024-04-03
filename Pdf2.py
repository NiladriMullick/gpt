from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import RectangleObject, NameObject, TextStringObject, IndirectObject

def highlight_word(input_pdf_path, output_pdf_path, word_to_highlight):
    # Open the input PDF
    with open(input_pdf_path, 'rb') as file:
        reader = PdfFileReader(file)
        writer = PdfFileWriter()

        # Iterate through each page of the PDF
        for page_number in range(reader.getNumPages()):
            page = reader.getPage(page_number)
            text = page.extractText()

            # Find all occurrences of the word on the page
            occurrences = []
            start = 0
            while True:
                start = text.find(word_to_highlight, start)
                if start == -1:
                    break
                end = start + len(word_to_highlight)
                occurrences.append((start, end))
                start = end

            # Add highlight annotations to the occurrences
            for start, end in occurrences:
                lower_left_x, lower_left_y, upper_right_x, upper_right_y = page.bbox.getLowerLeft()
                page_width = upper_right_x - lower_left_x
                page_height = upper_right_y - lower_left_y

                highlight = RectangleObject([lower_left_x, lower_left_y, upper_right_x, upper_right_y])
                highlight.upperLeft = (lower_left_x + start / len(text) * page_width, upper_right_y - page_height * 0.9)
                highlight.lowerRight = (lower_left_x + end / len(text) * page_width, upper_right_y - page_height * 0.95)
                highlight.setBorderColor((1, 1, 0))  # Yellow color
                highlight.update({
                    NameObject("/F"): 4,
                    NameObject("/Contents"): TextStringObject(""),
                })
                page.addAnnotation(highlight)

            writer.addPage(page)

        # Save the modified PDF with highlights
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

# Example usage:
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
output_pdf_path = 'highlighted_output.pdf'  # Replace with the path where you want to save the highlighted PDF
word_to_highlight = 'your_word_here'  # Replace with the word you want to highlight

highlight_word(input_pdf_path, output_pdf_path, word_to_highlight)
