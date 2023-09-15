"""
constants.py
------------

Description:
This module contains constants that are used across the application for file path generation,
data reading, and data exporting. It centralizes all the hard-coded values into one location
for easier management and future updates. This module is responsible for:
- Defining base directories and sub-folders where the input and output data are stored.
- Specifying filenames for industry data, QA data, and output files.
- Generating complete file paths for various data files using utility functions.
- Selecting relevant columns to be read from the QA data.

Modules:
- utils: Utility module to generate file paths.
"""

from utils import generate_file_path  # Utility function for generating file paths

# Define base directories and sub-folders
data_dir = '/Users/haoyunou/Desktop/ms-security/IPO业务问询项目/data/inputs'  # Base directory for input data
output_dir = '/Users/haoyunou/Desktop/ms-security/IPO业务问询项目/data/outputs'  # Base directory for output data
csv_sub_folder = '20230908'  # Sub-folder for storing CSV files

# Define filenames
industry_excel_filename = 'A股-行业0905.xlsx'  # Filename for the Excel file containing industry data
qa_csv_filenames = ['1.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv', '7.csv']  # Filenames for the CSV files containing QA data
output_txt_filename = 'ipo-qa-texts-20230915.txt'  # Filename for the output text file
output_csv_filename = 'ipo-qa-processed-20230915.csv'  # Filename for the output CSV file

# Generate file paths
excel_industry_filepath = generate_file_path(data_dir, filename=industry_excel_filename)  # File path for industry data
qa_csv_filepaths = [generate_file_path(data_dir, csv_sub_folder, filename) for filename in qa_csv_filenames]  # File paths for QA data
output_txt_filepath = generate_file_path(output_dir, filename=output_txt_filename)  # File path for output text file
output_csv_filepath = generate_file_path(output_dir, filename=output_csv_filename)  # File path for output CSV file

# Columns to read from the QA data
selected_columns = [
    "RN",
    "S_INFO_CODE",
    "S_INFO_NAME",
    "PROB_ID",
    "ANSW_TXT",
    "PROB_TXT",
    "SUP_ANSW_TXT",
]
