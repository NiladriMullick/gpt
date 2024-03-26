from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage

def insert_image_into_excel(image_path, excel_path, sheet_name, cell):
    # Open the Excel workbook
    wb = Workbook()
    ws = wb.active if sheet_name is None else wb[sheet_name]

    # Load the image
    img = ExcelImage(image_path)

    # Add the image to the worksheet at the specified cell
    ws.add_image(img, cell)

    # Save the workbook
    wb.save(excel_path)

# Example usage
image_path = 'image.jpg'  # Replace 'image.jpg' with the path to your image file
excel_path = 'output.xlsx'  # Specify the output Excel file path
sheet_name = 'Sheet1'  # Specify the name of the worksheet
cell = 'A1'  # Specify the cell where you want to insert the image (e.g., 'A1')

insert_image_into_excel(image_path, excel_path, sheet_name, cell)
