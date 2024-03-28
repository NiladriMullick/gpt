from styleframe import StyleFrame

# Load Excel files into StyleFrame objects
sf1 = StyleFrame.read_excel('file1.xlsx')
sf2 = StyleFrame.read_excel('file2.xlsx')

# Copy styles from the original StyleFrame objects
for column in sf2.columns:
    for cell in sf2[column]:
        original_cell = sf1[column][cell.row_index]
        if isinstance(original_cell, StyleFrame.Styler):
            cell.style = original_cell.style

# Save the merged data to the same workbook but different sheets
with StyleFrame.ExcelWriter('merged_file.xlsx') as writer:
    sf1.to_excel(writer, sheet_name='Sheet1', index=False)
    sf2.to_excel(writer, sheet_name='Sheet2', index=False)
