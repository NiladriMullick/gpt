from pdfminer.high_level import extract_text_to_fp
from io import StringIO

def pdf_to_html(input_pdf_path, output_html_path):
    # Open the input PDF
    with open(input_pdf_path, 'rb') as file:
        output_string = StringIO()

        # Extract text to a StringIO buffer
        extract_text_to_fp(file, output_string, output_type='html')

        # Write the HTML content to the output file
        with open(output_html_path, 'w') as output_file:
            output_file.write(output_string.getvalue())

# Example usage:
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
output_html_path = 'output.html'  # Replace with the path where you want to save the HTML file

pdf_to_html(input_pdf_path, output_html_path)
