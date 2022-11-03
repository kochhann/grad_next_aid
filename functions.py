import pandas as pd


def data_import_xls(file_name):
    data_dir = 'C:\\Dados\\'
    file = pd.ExcelFile(f'{data_dir}{file_name}')
    sheets = file.sheet_names
    print(sheets)
