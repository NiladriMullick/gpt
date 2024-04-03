from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import RectangleObject

def highlight_word(input_pdf_path, output_pdf_path, word_to_highlight):
    # Open the input PDF
    with open(input_pdf_path, 'rb') as file:
        reader = PdfFileReader(file)
        writer = PdfFileWriter()

        # Iterate through each page of the PDF
        for page_number in range(reader.getNumPages()):
            page = reader.getPage(page_number)
            annotations = page['/Annots'] if '/Annots' in page.keys() else []

            for annotation in annotations:
                if annotation['/Subtype'] == '/Highlight':
                    text = annotation.get_object()['/Contents']
                    if word_to_highlight.encode() in text:
                        rect = annotation['/Rect']
                        highlight = RectangleObject([rect[0], rect[1], rect[2], rect[3]])
                        highlight.upperLeft = (highlight.lowerLeft[0], highlight.upperLeft[1])
                        highlight.upperRight = (highlight.lowerRight[0], highlight.upperRight[1])
                        highlight.setBorderColor((1, 1, 0))  # Yellow color
                        highlight.update({
                            NameObject("/F"): 4,
                            NameObject("/Contents"): TextStringObject(""),
                            NameObject("/AP"): IndirectObject(annotation['/AP'].objid, 0)
                        })
                        page.annot_append(highlight)

            writer.addPage(page)

        # Save the modified PDF with highlights
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

# Example usage:
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
output_pdf_path = 'highlighted_output.pdf'  # Replace with the path where you want to save the highlighted PDF
word_to_highlight = 'your_word_here'  # Replace with the word you want to highlight

highlight_word(input_pdf_path, output_pdf_path, word_to_highlight)
