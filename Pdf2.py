from openpyxl import load_workbook

# Load the existing workbook
workbook = load_workbook('existing_workbook.xlsx')

# Access the active worksheet
worksheet = workbook.active

# Fill certain cells
worksheet['A1'] = 'Filled Data 1'
worksheet['B1'] = 'Filled Data 2'

# Save the workbook
workbook.save('filled_workbook.xlsx')
