from openpyxl import Workbook
from openpyxl.worksheet.hyperlink import Hyperlink

# Create a new workbook
workbook = Workbook()
worksheet = workbook.active

# Sample local directory paths of images
image_paths = [
    "/path/to/image1.png",
    "/path/to/image2.png",
    "/path/to/image3.png"
]

# Write the image paths to the Excel file and create hyperlinks
for i, path in enumerate(image_paths, start=1):
    cell = worksheet.cell(row=i, column=1)
    cell.value = "Image " + str(i)
    hyperlink = Hyperlink(location=path, display=path)
    cell.hyperlink = hyperlink

# Save the workbook
workbook.save('images_with_hyperlinks.xlsx')
