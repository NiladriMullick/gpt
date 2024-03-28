from openpyxl import load_workbook
from openpyxl.styles import Font, Color, Border, Side, PatternFill, Alignment

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
        # Preserve font attributes
        new_font = Font(name=cell.font.name, size=cell.font.size, bold=cell.font.bold, italic=cell.font.italic,
                        vertAlign=cell.font.vertAlign, underline=cell.font.underline, strike=cell.font.strike,
                        color=cell.font.color, family=cell.font.family)
        new_cell.font = new_font
        # Preserve fill color
        if cell.fill is not None:
            new_fill = PatternFill(fill_type=cell.fill.fill_type, fgColor=cell.fill.fgColor, bgColor=cell.fill.bgColor)
            new_cell.fill = new_fill
        # Preserve border
        if cell.border is not None:
            new_border = Border(left=Side(border_style=cell.border.left.style, color=cell.border.left.color),
                                right=Side(border_style=cell.border.right.style, color=cell.border.right.color),
                                top=Side(border_style=cell.border.top.style, color=cell.border.top.color),
                                bottom=Side(border_style=cell.border.bottom.style, color=cell.border.bottom.color))
            new_cell.border = new_border
        # Preserve alignment
        new_alignment = Alignment(horizontal=cell.alignment.horizontal, vertical=cell.alignment.vertical,
                                   text_rotation=cell.alignment.text_rotation, wrap_text=cell.alignment.wrap_text,
                                   shrink_to_fit=cell.alignment.shrink_to_fit, indent=cell.alignment.indent)
        new_cell.alignment = new_alignment

# Save the merged workbook
wb1.save('merged_file.xlsx')
