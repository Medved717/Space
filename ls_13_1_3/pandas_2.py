# import pandas as pd
#
# # Предположим, у нас есть DataFrame df с данными о винах
# df = pd.DataFrame({
#     'country': ['France', 'Italy', 'Spain', 'France', 'Italy', 'Spain'],
#     'price': [20, 15, 30, 22, 18, 25]
# })
#
# # Группировка данных по странам
# country_grouped = df.groupby('country')
#
# # Вычисление средней цены для каждой страны
# mean_price_by_country = country_grouped['price'].mean()
# print(mean_price_by_country)

import pandas as pd
import numpy as np

data_with_nan = {
    'Name': ['John', 'Anna', 'Peter', None, 'Bob'],
    'Age': [28, np.nan, 29, 42, 37],
    'Salary': [75000, 82000, 67000, 95000, 90000]
}

df_nan = pd.DataFrame(data_with_nan)

sorted_df_nan = df_nan.sort_values(by='Age', na_position='first')
print(sorted_df_nan)
