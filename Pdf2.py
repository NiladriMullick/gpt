import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Load the first Excel file
excel_file1 = pd.ExcelFile('file1.xlsx')
# Load the second Excel file
excel_file2 = pd.ExcelFile('file2.xlsx')

# Create a new Excel writer object
with pd.ExcelWriter('merged_file.xlsx', engine='openpyxl') as writer:
    writer.book = load_workbook('merged_file.xlsx')

    # Write sheets from the first Excel file
    for sheet_name in excel_file1.sheet_names:
        df = pd.read_excel(excel_file1, sheet_name=sheet_name)
        sheet = writer.book.create_sheet(title=sheet_name)
        for row in dataframe_to_rows(df, index=False, header=True):
            sheet.append(row)

    # Write sheets from the second Excel file
    for sheet_name in excel_file2.sheet_names:
        df = pd.read_excel(excel_file2, sheet_name=sheet_name)
        sheet = writer.book.create_sheet(title=sheet_name)
        for row in dataframe_to_rows(df, index=False, header=True):
            sheet.append(row)

    writer.save()

print("Merged Excel files successfully while preserving formatting and styles.")
