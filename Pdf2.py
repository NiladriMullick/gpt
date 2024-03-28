from openpyxl import load_workbook
from openpyxl.styles import NamedStyle

# Load the first Excel file
wb1 = load_workbook('file1.xlsx')

# Load the second Excel file
wb2 = load_workbook('file2.xlsx')

# Create a new workbook to combine the sheets
combined_wb = load_workbook()

# Copy styles from source to destination
def copy_style(source, destination):
    for style in source._cell_styles.values():
        new_style = NamedStyle(name=style.name)
        new_style.font = style.font
        destination._cell_styles[style.name] = new_style

# Copy sheets from the first workbook to the combined workbook
for sheet in wb1.sheetnames:
    source = wb1[sheet]
    destination = combined_wb.create_sheet(title=sheet)
    
    for row in source.iter_rows():
        for cell in row:
            destination[cell.coordinate].value = cell.value
            if cell.has_style:
                copy_style(cell, destination[cell.coordinate])

# Copy sheets from the second workbook to the combined workbook
for sheet in wb2.sheetnames:
    source = wb2[sheet]
    destination = combined_wb.create_sheet(title=sheet)
    
    for row in source.iter_rows():
        for cell in row:
            destination[cell.coordinate].value = cell.value
            if cell.has_style:
                copy_style(cell, destination[cell.coordinate])

# Save the combined workbook
combined_wb.save('combined_workbook.xlsx')
