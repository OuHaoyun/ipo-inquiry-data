import pandas as pd

from utils import prepare_qa_data, export_df_to_txt
from constants import (excel_industry_filepath,
                       qa_csv_filepaths,
                       selected_columns,
                       output_csv_filepath,
                       output_txt_filepath)


if __name__ == '__main__':
    # Load industry file
    df_industry = pd.read_excel(excel_industry_filepath, engine="openpyxl")
    
    # Process the QA data
    df_final = prepare_qa_data(qa_csv_filepaths, df_industry, selected_columns)
    
    # Export a txt file of QA pairs
    export_df_to_txt(df_final, output_txt_filepath)
    df_final.to_csv(output_csv_filepath)
