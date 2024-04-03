from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.pdf import PageObject

def highlight_word(input_pdf_path, output_pdf_path, word_to_highlight):
    # Open the input PDF
    with open(input_pdf_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        # Iterate through each page of the PDF
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            if '/Annots' in page:
                annots = page['/Annots']
                for annot in annots:
                    if annot['/Subtype'] == '/Highlight':
                        text = annot.get_object()['/Contents']
                        if word_to_highlight.encode() in text:
                            page_annot = PageObject.create_page(None, annot)
                            page_annot.extract_text()
                            writer.add_page(page_annot)

        # Save the modified PDF with highlights
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

# Example usage:
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
output_pdf_path = 'highlighted_output.pdf'  # Replace with the path where you want to save the highlighted PDF
word_to_highlight = 'your_word_here'  # Replace with the word you want to highlight

highlight_word(input_pdf_path, output_pdf_path, word_to_highlight)
