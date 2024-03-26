import os
import fitz  # PyMuPDF

def split_pdf(input_pdf_path, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the input PDF file
    pdf_document = fitz.open(input_pdf_path)

    # Iterate over each page in the PDF
    for page_number in range(pdf_document.page_count):
        # Get the current page
        page = pdf_document.load_page(page_number)

        # Create the output PDF file path
        output_pdf_path = os.path.join(output_folder, f'{page_number + 1}.pdf')

        # Create a new PDF document containing only the current page
        new_document = fitz.open()
        new_document.insert_pdf(pdf_document, from_page=page_number, to_page=page_number)

        # Save the new document as a separate PDF file
        new_document.save(output_pdf_path)
        new_document.close()

    # Close the original PDF document
    pdf_document.close()

# Example usage
input_pdf_path = 'input.pdf'  # Replace 'input.pdf' with the path to your PDF file
output_folder = 'output_folder'  # Specify the output folder where individual PDFs will be saved
split_pdf(input_pdf_path, output_folder)
