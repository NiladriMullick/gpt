from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

# Load the first Excel file
wb1 = load_workbook('file1.xlsx')

# Load the second Excel file
wb2 = load_workbook('file2.xlsx')

# Create a new workbook to combine the sheets
combined_wb = load_workbook()

# Copy sheets from the first workbook to the combined workbook
for sheet in wb1.sheetnames:
    source = wb1[sheet]
    destination = combined_wb.create_sheet(title=sheet)
    
    for row in source.iter_rows():
        for cell in row:
            destination[cell.coordinate].value = cell.value
            destination[cell.coordinate].font = cell.font  # Copying font style

# Copy sheets from the second workbook to the combined workbook
for sheet in wb2.sheetnames:
    source = wb2[sheet]
    destination = combined_wb.create_sheet(title=sheet)
    
    for row in source.iter_rows():
        for cell in row:
            destination[cell.coordinate].value = cell.value
            destination[cell.coordinate].font = cell.font  # Copying font style

# Save the combined workbook
combined_wb.save('combined_workbook.xlsx')
