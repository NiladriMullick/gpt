import os
from PyPDF2 import PdfFileReader, PdfWriter

def split_pdf(input_pdf_path, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the input PDF file
    with open(input_pdf_path, 'rb') as file:
        reader = PdfFileReader(file)

        # Iterate over each page in the PDF
        for page_num in range(reader.numPages):
            # Create a PdfWriter object for the current page
            writer = PdfWriter()

            # Add the current page to the PdfWriter object
            writer.add_page(reader.getPage(page_num))

            # Create the output PDF file path
            output_pdf_path = os.path.join(output_folder, f'{page_num + 1}.pdf')

            # Write the current page to the output PDF file
            with open(output_pdf_path, 'wb') as output_file:
                writer.write(output_file)

# Example usage
input_pdf_path = 'input.pdf'  # Replace 'input.pdf' with the path to your PDF file
output_folder = 'output_folder'  # Specify the output folder where individual PDFs will be saved
split_pdf(input_pdf_path, output_folder)
