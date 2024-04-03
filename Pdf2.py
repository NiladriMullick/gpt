from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def highlight_word(input_pdf_path, output_pdf_path, word_to_highlight):
    # Open the input PDF
    with open(input_pdf_path, 'rb') as file:
        reader = PdfFileReader(file)
        writer = PdfFileWriter()

        # Iterate through each page of the PDF
        for page_number in range(reader.getNumPages()):
            page = reader.getPage(page_number)
            pdf_data = BytesIO()
            pdf_canvas = canvas.Canvas(pdf_data, pagesize=letter)
            pdf_canvas.setFont("Times-Roman", 12)

            text = page.extractText()
            text_objects = text.split(word_to_highlight)
            x = 0
            for i, text_part in enumerate(text_objects):
                # Draw text
                pdf_canvas.drawString(x, 0, text_part)
                x += pdf_canvas.stringWidth(text_part, "Times-Roman", 12)

                # Highlight word
                if i < len(text_objects) - 1:
                    # Get position for highlighting
                    word_width = pdf_canvas.stringWidth(word_to_highlight, "Times-Roman", 12)
                    x += pdf_canvas.stringWidth(word_to_highlight, "Times-Roman", 12) / 2
                    y = 10  # Adjust this value based on your requirements

                    # Draw highlight
                    pdf_canvas.setFillColorRGB(1, 1, 0)  # Yellow color (RGB values)
                    pdf_canvas.setStrokeColorRGB(1, 1, 0)  # Yellow color for outline as well
                    pdf_canvas.rect(x, y, word_width, 12, stroke=1, fill=1)

            pdf_canvas.save()

            # Merge the highlighted page with the original page
            pdf_data.seek(0)
            highlight_page = PdfFileReader(pdf_data).getPage(0)
            page.merge_page(highlight_page)
            writer.addPage(page)

        # Save the modified PDF with highlights
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

# Example usage:
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
output_pdf_path = 'highlighted_output.pdf'  # Replace with the path where you want to save the highlighted PDF
word_to_highlight = 'your_word_here'  # Replace with the word you want to highlight

highlight_word(input_pdf_path, output_pdf_path, word_to_highlight)
