from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

# Load both Excel files
wb1 = load_workbook('file1.xlsx')
wb2 = load_workbook('file2.xlsx')

# Get the sheets you want to merge from each workbook
ws1 = wb1.active
ws2 = wb2.active

# Copy data and formatting from one sheet to another
for row in ws2.iter_rows(min_row=1, max_row=ws2.max_row, min_col=1, max_col=ws2.max_column):
    for cell in row:
        new_cell = ws1.cell(row=ws1.max_row + 1, column=cell.column, value=cell.value)
        new_cell.font = cell.font  # Preserve font
        new_cell.fill = cell.fill  # Preserve fill color
        new_cell.border = cell.border  # Preserve border
        new_cell.number_format = cell.number_format  # Preserve number format
        new_cell.alignment = cell.alignment  # Preserve alignment

# Save the merged workbook
wb1.save('merged_file.xlsx')
