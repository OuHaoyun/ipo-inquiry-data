"""
utils.py
--------

Description:
This utility module contains a collection of helper functions for file path generation,
text cleaning, and data processing. It provides functionalities for preparing and exporting
QA data. Specifically, it includes functions to:
- Generate complete file paths based on directory, sub-folder, and filename.
- Clean specified text columns in a DataFrame by removing HTML tags and special characters.
- Process QA data by reading from multiple CSV files, merging with industry data,
  filtering and sorting.
- Export processed data to a text file.

Functions:
- generate_file_path(base_path: str, sub_folder: Optional[str] = None, filename: Optional[str] = None) -> str
- clean_text_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame
- prepare_qa_data(csv_filepaths: List[str], df_industry: pd.DataFrame, selected_cols: Optional[List[str]] = None) -> pd.DataFrame
- export_df_to_txt(df: pd.DataFrame, file_path: str) -> None

Modules:
- os: Provides a way of using operating system dependent functionality like reading or writing to the file system.
- re: Provides regular expression matching operations for string parsing and manipulation.
- pandas: Provides high-performance, easy-to-use data structures and data analysis tools.
- typing: Provides runtime support for type hints, enhancing code readability and reusability.
"""


# Standard library imports
import os  # Provides a way of using operating system dependent functionality like reading or writing to the file system
import re  # Provides regular expression matching operations for string parsing and manipulation

# For type hinting and annotations
from typing import List, Optional  # Provides runtime support for type hints, enhancing code readability and reusability

# Third-party imports
import pandas as pd  # Provides high-performance, easy-to-use data structures and data analysis tools


def generate_file_path(
    base_path: str, sub_folder: Optional[str] = None, filename: Optional[str] = None
) -> str:
    """Generates a complete file path.

    Args:
        base_path (str): The base directory path.
        sub_folder (str, optional): The sub-folder under the base directory.
        filename (str, optional): The name of the file.

    Returns:
        str: The complete file path.
    """
    if sub_folder:
        base_path = os.path.join(base_path, sub_folder)
    if filename:
        return os.path.join(base_path, filename)
    return base_path


def clean_text_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Cleans specified text columns in a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to clean.
        columns (List[str]): The list of column names to clean.

    Returns:
        pd.DataFrame: A DataFrame with cleaned text columns.
    """
    df_cleaned = df.copy()
    for col in columns:
        # Convert to string type if not already
        df_cleaned[col] = df_cleaned[col].astype(str)

        # Remove HTML tags and special characters
        df_cleaned[col] = df_cleaned[col].apply(lambda x: re.sub(r"<.*?>", "", x))
        df_cleaned[col] = df_cleaned[col].str.replace("？", "", regex=False)
        df_cleaned[col] = df_cleaned[col].str.replace("\u3000", " ", regex=False)
        df_cleaned[col] = df_cleaned[col].str.replace("�", "", regex=False)

    return df_cleaned


def prepare_qa_data(
    csv_filepaths: List[str],
    df_industry: pd.DataFrame,
    selected_cols: Optional[List[str]] = None,
) -> pd.DataFrame:
    """Prepares and processes QA data from multiple CSV files.

    Args:
        csv_filepaths (List[str]): List of CSV file paths to read.
        df_industry (pd.DataFrame): DataFrame with industry information.
        selected_cols (List[str], optional): Columns to select from the CSVs.

    Returns:
        pd.DataFrame: Processed DataFrame combining all the QA data.
    """
    processed_dfs_list = []
    data_type = {"RN": "object", "PROB_ID": "object", "S_INFO_CODE": "object"}
    text_cols = ["ANSW_TXT", "PROB_TXT", "SUP_ANSW_TXT"]

    for filepath in csv_filepaths:
        with open(filepath, "r", encoding="gb2312", errors="replace") as f:
            df = pd.read_csv(f, usecols=selected_cols, dtype=data_type)

        df = df.dropna(subset=["ANSW_TXT", "PROB_TXT"])
        df_tgf = df[df["PROB_TXT"].str.contains("推广费", case=False, na=False)]
        df_merged = pd.merge(
            df_tgf,
            df_industry[["S_INFO_CODE", "INDUSTRY_LEVEL_1"]],
            on="S_INFO_CODE",
            how="left",
        )
        df_yysw = df_merged[df_merged.INDUSTRY_LEVEL_1 == "医药生物"]
        df_cleaned = clean_text_columns(df_yysw, text_cols)
        processed_dfs_list.append(df_cleaned)

    df_final = pd.concat(processed_dfs_list, ignore_index=True)
    df_final = df_final.sort_values(by="PROB_ID", ascending=True).reset_index(drop=True)

    return df_final


def export_df_to_txt(df: pd.DataFrame, file_path: str) -> None:
    """Exports a DataFrame to a TXT file.

    Args:
        df (pd.DataFrame): The DataFrame to export.
        file_path (str): The file path to save the TXT file.

    Returns:
        None
    """
    print("Starting to write file...")
    with open(file_path, "w", encoding="utf-8") as f:
        for index, row in df.iterrows():
            f.write(f"问题序号: {row['PROB_ID']}\n")
            f.write("提问:\n")
            f.write(f"{row['PROB_TXT']}\n")
            f.write("回答:\n")
            f.write(f"{row['ANSW_TXT']}\n")
            f.write("补充回答:\n")
            sup_answ_txt = row["SUP_ANSW_TXT"] if row["SUP_ANSW_TXT"] != "nan" else "无"
            f.write(f"{sup_answ_txt}\n\n")
    print("File written successfully.")
