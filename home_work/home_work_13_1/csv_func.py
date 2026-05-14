import pandas as pd
import json
import os

transactions_puth = os.path.join('transactions.csv')


def reading_csv_transactions(transactions_puth):
    df_transactions_csv = pd.read_csv(transactions_puth)
    transactions_dict = df_transactions_csv.to_dict()
    return transactions_dict


print(reading_csv_transactions(transactions_puth))
