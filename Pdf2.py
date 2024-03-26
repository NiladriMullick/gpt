from openpyxl import load_workbook
from openpyxl.drawing.image import Image as ExcelImage

def insert_image_into_excel(image_path, excel_path, sheet_name, cell):
    # Load the existing Excel workbook
    wb = load_workbook(excel_path)
    ws = wb[sheet_name]

    # Load the image
    img = ExcelImage(image_path)

    # Add the image to the worksheet at the specified cell
    ws.add_image(img, cell)

    # Adjust the dimensions of the cell to accommodate the image
    ws.column_dimensions[cell[0]].width = img.width / 7
    ws.row_dimensions[int(cell[1:])].height = img.height / 7

    # Save the workbook
    wb.save(excel_path)

# Example usage
image_path = 'image.jpg'  # Replace 'image.jpg' with the path to your image file
excel_path = 'existing_workbook.xlsx'  # Specify the path to the existing Excel workbook
sheet_name = 'Sheet1'  # Specify the name of the worksheet
cell = 'A1'  # Specify the cell where you want to insert the image (e.g., 'A1')

insert_image_into_excel(image_path, excel_path, sheet_name, cell)
