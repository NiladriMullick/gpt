from pdfminer.high_level import extract_text_to_fp
from io import BytesIO

def pdf_to_html(input_pdf_path, output_html_path):
    # Open the input PDF
    with open(input_pdf_path, 'rb') as file:
        output_bytes = BytesIO()

        # Extract text to a BytesIO buffer
        extract_text_to_fp(file, output_bytes, output_type='html')

        # Convert BytesIO content to string
        html_content = output_bytes.getvalue().decode('utf-8')

        # Write the HTML content to the output file
        with open(output_html_path, 'w', encoding='utf-8') as output_file:
            output_file.write(html_content)

# Example usage:
input_pdf_path = 'input.pdf'  # Replace with your input PDF file path
output_html_path = 'output.html'  # Replace with the path where you want to save the HTML file

pdf_to_html(input_pdf_path, output_html_path)
