from openpyxl import load_workbook
from openpyxl.styles import Font
import itertools

def make_words_bold(excel_path):
    # Load the workbook
    wb = load_workbook(excel_path)
    ws = wb.active

    # Get the data from the columns
    matched_column = list(ws['A'])
    content_column = list(ws['B'])

    # Iterate through rows
    for matched_cell, content_cell in zip(matched_column[1:], content_column[1:]):  # Skipping the header row
        matched_words = matched_cell.value.split(',')
        content = content_cell.value

        # Split the content into parts based on spaces
        parts = content.split()

        # Initialize a variable to store the formatted content
        formatted_content = []

        # Iterate through parts to find and make the target words bold
        for part in parts:
            if part in matched_words:
                # Make the word bold and add it to the formatted content
                formatted_content.append(Font(bold=True))
            else:
                # Add the part as is to the formatted content
                formatted_content.append(part)

        # Join the formatted content back into a string
        formatted_string = ' '.join(formatted_content)

        # Update the content cell with the formatted content
        content_cell.value = formatted_string

    # Save the workbook
    wb.save(excel_path)

# Example usage:
make_words_bold("example.xlsx")
