from openpyxl import load_workbook

# Load both Excel files
wb1 = load_workbook('file1.xlsx')
wb2 = load_workbook('file2.xlsx')

# Get the sheets you want to merge from each workbook
ws1 = wb1['Sheet1']
ws2 = wb2['Sheet1']

# Copy data and formatting from one sheet to another
for row in ws2.iter_rows(min_row=2, max_row=ws2.max_row, min_col=1, max_col=ws2.max_column):
    new_row = [cell.value for cell in row]
    ws1.append(new_row)

# Save the merged workbook
wb1.save('merged_file.xlsx')
