import pandas as pd

data = {'Имя игрушки': ['Мишка', 'Зайка', 'Робот'], 'Цвет': ['Коричневый', 'Розовый', 'Серый'],
        'Размер': ['Большой', 'Маленький', 'Средний'], 'Цена': [500, 300, 700]}

df = pd.DataFrame(data)
df = df.set_index(keys='Имя игрушки', drop=True, append=False, inplace=False)


new_df = df.loc[df['Цвет'].isin(['Коричневый', 'Серый']) & df['Размер'].isin(['Маленький', 'Средний'])]

print(new_df)

