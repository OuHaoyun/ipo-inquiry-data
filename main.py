from utility import *
from constants import *

if __name__ == '__main__':
    # Load industry file
    df_industry = pd.read_excel(excel_industry_filepath, engine="openpyxl")
    
    # Process the QA data
    df_final = prepare_qa_data(qa_csv_filepaths, df_industry)
    
    # Export a txt file of QA pairs
    export_df_to_txt(df_final, output_txt_filepath)
    df_final.to_csv(output_csv_filepath)





