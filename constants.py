import os

# Industry information Excel file path
excel_industry_filepath = '/Users/haoyunou/Desktop/ms-security/IPO业务问询项目/A股-行业0905.xlsx'

# QA csv file paths
data_dir = '/Users/haoyunou/Desktop/ms-security/IPO业务问询项目/20230908/'
qa_csv_filenames = ['1.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv', '7.csv']
qa_csv_filepaths = [os.path.join(data_dir, qa_file_name) for qa_file_name in qa_csv_filenames]

# Export file paths
output_txt_filepath = 'ipo-qa-texts-20230915.txt'
output_csv_filepath = 'ipo-qa-processed-20230915.csv'
