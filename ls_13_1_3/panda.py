import pandas as pd

# pd = pd.DataFrame({'Yes': [123, 456, 959], 'No': [234, 25425, 435]}, index=['Good', 'Bad', 'Normal'])
# print(pd)


# s = pd.Series([1, 2, 3, 4, 5, 6, 7],
#               index=['Темп роста в 2018', 'Темп роста в 2019 году', 'Темп роста в 2020 году', 'Темп роста в 2021 году',
#                      'Темп роста в 2022 году', 'Темп роста в 2023 году', 'Темп роста в 2024 году'],
#               name='Какая-то фигня')
#
# print(s)

wine_reviews = pd.read_excel('winemag-data-130k-v2.xlsx')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(wine_reviews)





