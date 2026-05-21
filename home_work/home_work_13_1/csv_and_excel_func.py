import pandas as pd
import os

transactions_puth_csv = os.path.join('transactions.csv')


def reading_csv_transactions(transactions_puth_csv):
    df_transactions_csv = pd.read_csv(transactions_puth_csv)
    transactions_dict = df_transactions_csv.to_dict('records')
    return transactions_dict


transactions_puth_excel = os.path.join('transactions_excel.xlsx')


def reading_excel_transactions(transactions_puth_excel):
    df_transactions_excel = pd.read_excel(transactions_puth_excel)
    df_transactions_dict = df_transactions_excel.to_dict('records')
    return df_transactions_dict

print(reading_excel_transactions(transactions_puth_excel))