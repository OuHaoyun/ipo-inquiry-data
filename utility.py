import pandas as pd
# from pandas import DataFrame
import re


def clean_text_columns(df, columns):
    df_cleaned = df.copy()
    for col in columns:
        # Convert to string type if not already
        df_cleaned[col] = df_cleaned[col].astype(str)

        # Remove HTML tags
        df_cleaned[col] = df_cleaned[col].apply(lambda x: re.sub(r"<.*?>", "", x))

        # Remove special characters like "？","\u3000", and "�"
        df_cleaned[col] = df_cleaned[col].str.replace("？", "", regex=False)
        df_cleaned[col] = df_cleaned[col].str.replace("\u3000", " ", regex=False)
        df_cleaned[col] = df_cleaned[col].str.replace("�", "", regex=False)

    return df_cleaned


def prepare_qa_data(
    csv_filepaths,
    df_industry,
    selected_cols=[
        "RN",
        "S_INFO_CODE",
        "S_INFO_NAME",
        "PROB_ID",
        "ANSW_TXT",
        "PROB_TXT",
        "SUP_ANSW_TXT",
    ],
):
    processed_dfs = []  # List to store processed DataFrames

    data_type = {"RN": "object", "PROB_ID": "object", "S_INFO_CODE": "object"}

    text_cols = ["ANSW_TXT", "PROB_TXT", "SUP_ANSW_TXT"]

    for filepath in csv_filepaths:
        with open(filepath, "r", encoding="gb2312", errors="replace") as f:
            df = pd.read_csv(f, usecols=selected_cols, dtype=data_type)

        # Drop NA values
        df = df.dropna(subset=["ANSW_TXT", "PROB_TXT"])

        # Filter rows containing "推广费"
        df_tgf = df[df["PROB_TXT"].str.contains("推广费", case=False, na=False)]

        # Merge with industry DataFrame
        df_merged = pd.merge(
            df_tgf,
            df_industry[["S_INFO_CODE", "INDUSTRY_LEVEL_1"]],
            on="S_INFO_CODE",
            how="left",
        )

        # Filter rows where INDUSTRY_LEVEL_1 is "医药生物"
        df_yysw = df_merged[df_merged.INDUSTRY_LEVEL_1 == "医药生物"]

        # Clean text columns
        df_cleaned = clean_text_columns(df_yysw, text_cols)

        # Append the cleaned DataFrame to the list
        processed_dfs.append(df_cleaned)

        # Concat the processed dfs and sort by 'PROB_ID'
        df_final = pd.concat(processed_dfs, ignore_index=True)
        df_final = df_final.sort_values(by="PROB_ID", ascending=True).reset_index(
            drop=True
        )

    return df_final


def export_df_to_txt(df: pd.DataFrame, file_path: str) -> None:
    print("Starting to write file...")
    with open(file_path, "w", encoding="utf-8") as f:
        for index, row in df.iterrows():
            f.write(f"问题序号: {row['PROB_ID']}\n")
            f.write("提问:\n")
            f.write(f"{row['PROB_TXT']}\n")
            f.write("回答:\n")
            f.write(f"{row['ANSW_TXT']}\n")
            f.write("补充回答:\n")

            # Check if 'SUP_ANSW_TXT' is NaN, and write "无" if it is
            sup_answ_txt = row["SUP_ANSW_TXT"] if row["SUP_ANSW_TXT"] != "nan" else "无"
            f.write(f"{sup_answ_txt}\n\n")
    print("File written successfully.")
