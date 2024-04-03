from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def highlight_word(input_pdf_path, output_pdf_path, word_to_highlight):
    # Open the input PDF
    with open(input_pdf_path, 'rb') as file:
        reader = PdfFileReader(file)
        writer = PdfFileWriter()

        # Iterate through each page of the PDF
        for page_number in range(reader.getNumPages()):
            page = reader.getPage(page_number)
            pdf_canvas = canvas.Canvas(f"{page_number}.pdf", pagesize=letter)
            pdf_canvas.setLineWidth(1)
            pdf_canvas.setStrokeColorRGB(1, 0, 0)  # Set highlight color to red

            text_objects = page.extractText().split(word_to_highlight)
            x = 0
            for text in text_objects[:-1]:
                x += pdf_canvas.stringWidth(text, "Times-Roman", 12)
                pdf_canvas.drawString(x, 0, text)
                x += pdf_canvas.stringWidth(word_to_highlight, "Times-Roman", 12)
                pdf_canvas.setFillColorRGB(1, 1, 0)  # Set fill color to yellow
                pdf_canvas.drawString(x, 0, word_to_highlight)
                pdf_canvas.setStrokeColorRGB(1, 0, 0)  # Reset stroke color to red
            pdf_canvas.save()

            # Merge the highlighted page with the original page
            with open(f"{page_number}.pdf", 'rb') as highlight_file:
                highlight_page = PdfFileReader(highlight_file).getPage(0)
                page.merge_page(highlight_page)
                writer.addPage(page)

    # Save the modified PDF with highlights
    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)

    # Clean up temporary files
    for page_number in range(reader.getNumPages()):
        os.remove(f"{page_number}.pdf")

# Example usage:
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
output_pdf_path = 'highlighted_output.pdf'  # Replace with the path where you want to save the highlighted PDF
word_to_highlight = 'your_word_here'  # Replace with the word you want to highlight

highlight_word(input_pdf_path, output_pdf_path, word_to_highlight)
