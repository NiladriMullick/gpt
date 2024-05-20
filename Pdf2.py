import pandas as pd
import os

# Define the directory containing the Excel files
directory = 'path/to/your/excel/files'

# List all Excel files in the directory
excel_files = [file for file in os.listdir(directory) if file.endswith('.xlsx') or file.endswith('.xls')]

# Read each Excel file into a DataFrame and store them in a list
dataframes = []
for file in excel_files:
    file_path = os.path.join(directory, file)
    df = pd.read_excel(file_path)
    dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
concatenated_df = pd.concat(dataframes, ignore_index=True)

# (Optional) Save the concatenated DataFrame to a new Excel file
output_file = 'path/to/output/concatenated_file.xlsx'
concatenated_df.to_excel(output_file, index=False)
