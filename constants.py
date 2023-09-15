from utility import generate_file_path

# Define base directories and sub-folders
data_dir = '/Users/haoyunou/Desktop/ms-security/IPO业务问询项目/data/inputs'
output_dir = '/Users/haoyunou/Desktop/ms-security/IPO业务问询项目/data/outputs'
csv_sub_folder = '20230908'

# Define filenames
industry_excel_filename = 'A股-行业0905.xlsx'
qa_csv_filenames = ['1.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv', '7.csv']
output_txt_filename = 'ipo-qa-texts-20230915.txt'
output_csv_filename = 'ipo-qa-processed-20230915.csv'

# Generate file paths
excel_industry_filepath = generate_file_path(data_dir, filename=industry_excel_filename)
qa_csv_filepaths = [generate_file_path(data_dir, csv_sub_folder, filename) for filename in qa_csv_filenames]
output_txt_filepath = generate_file_path(output_dir, filename=output_txt_filename)
output_csv_filepath = generate_file_path(output_dir, filename=output_csv_filename)

# Select relevant columns to be read from QA data
selected_columns = [
        "RN",
        "S_INFO_CODE",
        "S_INFO_NAME",
        "PROB_ID",
        "ANSW_TXT",
        "PROB_TXT",
        "SUP_ANSW_TXT",
    ]