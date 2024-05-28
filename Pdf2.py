import pandas as pd
import os

# Directory containing the Excel files
directory = '/path/to/your/excel/files'

# Initialize an empty list to hold the DataFrames
dataframes = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Read the specific sheet into a DataFrame
        try:
            df = pd.read_excel(file_path, sheet_name='AllArticles')
            dataframes.append(df)
        except Exception as e:
            print(f"Could not read sheet 'AllArticles' from file {filename}: {e}")

# Concatenate all the DataFrames into one
combined_df = pd.concat(dataframes, ignore_index=True)

# Optionally, save the combined DataFrame to a new Excel file
# combined_df.to_excel('/path/to/save/combined_data.xlsx', index=False)

print(combined_df)
