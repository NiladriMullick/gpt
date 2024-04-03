from pdfrw import PdfReader, PdfWriter, PageObject, PdfDict

def highlight_word(input_pdf_path, output_pdf_path, word_to_highlight):
    # Open the input PDF
    input_pdf = PdfReader(input_pdf_path)
    output_pdf = PdfWriter()

    # Iterate through each page of the PDF
    for page in input_pdf.pages:
        # Extract text from the page
        text = page.extract_text()
        
        # Check if the word is present in the text
        if word_to_highlight in text:
            # Find the position of the word
            start_index = text.find(word_to_highlight)
            end_index = start_index + len(word_to_highlight)

            # Get the coordinates of the word on the page
            x0, y0, x1, y1 = page.MediaBox[0], page.MediaBox[1], page.MediaBox[2], page.MediaBox[3]

            # Add highlight annotation to the word's position
            annot = PageObject.create_annotation('Highlight',
                                                 Rect=[x0, y0, x1, y1],
                                                 Contents='',
                                                 QuadPoints=[x0, y0, x1, y0, x0, y1, x1, y1])
            page[Annots] = page.get('/Annots', []) + [annot]

        # Add the modified page to the output PDF
        output_pdf.addpage(page)

    # Save the modified PDF with highlights
    output_pdf.write(output_pdf_path)

# Example usage:
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
output_pdf_path = 'highlighted_output.pdf'  # Replace with the path where you want to save the highlighted PDF
word_to_highlight = 'your_word_here'  # Replace with the word you want to highlight

highlight_word(input_pdf_path, output_pdf_path, word_to_highlight)
