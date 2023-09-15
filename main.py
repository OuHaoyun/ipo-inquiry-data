"""
main.py
-------

Description:
This script loads an industry Excel file and QA data from multiple CSV files.
It processes the data by merging it with industry information, filtering,
and cleaning text fields. The processed data is then exported to a text file
and a CSV file.

Expected Inputs:
- An Excel file with industry information.
- Multiple CSV files with QA data.

Outputs:
- A text file containing processed QA pairs.
- A CSV file containing the processed data.
"""

# Third-party imports
import pandas as pd  # Provides high-performance, easy-to-use data structures and data analysis tools

# Local imports
from utils import (
    prepare_qa_data,
    export_df_to_txt,
)  # Utility functions for data preparation and export
from constants import (  # Constants including file paths and selected columns
    excel_industry_filepath,
    qa_csv_filepaths,
    selected_columns,
    output_csv_filepath,
    output_txt_filepath,
)

if __name__ == "__main__":
    # Load the industry Excel file into a DataFrame
    df_industry = pd.read_excel(excel_industry_filepath, engine="openpyxl")

    # Process QA data from multiple CSV files and merge with industry information
    df_final = prepare_qa_data(qa_csv_filepaths, df_industry, selected_columns)

    # Export the processed QA pairs to a text file
    export_df_to_txt(df_final, output_txt_filepath)

    # Export the processed DataFrame to a CSV file
    df_final.to_csv(output_csv_filepath)
