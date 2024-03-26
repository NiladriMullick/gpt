import PyPDF2

def highlight_words(pdf_path, words_to_highlight, output_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        writer = PyPDF2.PdfFileWriter()
        
        # Loop through each page
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text = page.extractText()
            
            # Search for words in the list and highlight them
            for word in words_to_highlight:
                if word in text:
                    # Replace the word with a highlighted version
                    highlighted_text = text.replace(word, f'<span style="background-color: yellow;">{word}</span>')
                    page.mergePage(PyPDF2.PdfFileReader(highlighted_text).getPage(0))
            
            # Add the modified page to the new PDF
            writer.addPage(page)
        
        # Save the modified PDF
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

# Example usage
pdf_path = 'example.pdf'
words_to_highlight = ['example', 'words', 'list']
output_path = 'highlighted.pdf'
highlight_words(pdf_path, words_to_highlight, output_path)
