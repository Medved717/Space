# Задача 1
# Напишите функцию, которая принимает на вход DataFrame из датасета titanic.csv.
# Функция должна вычислить средний возраст мужчин и женщин отдельно и вернуть результат в виде словаря в формате JSON.

# import pandas as pd
# import json
#
# df = pd.read_csv('titanic.csv')
#
#
# def titanic_list(df):
#     man_list = df[df['Sex'] == 'male']['Age'].mean()
#     women_list = df[df['Sex'] == 'female']['Age'].mean()
#     result = f'Мужчины: {man_list}, Женщины: {women_list}'
#     return json.dumps(result, ensure_ascii=False)
#
# result = titanic_list(df)
# print(result)
#
# ensure_ascii=False


# Задача 2 Напишите функцию, которая должна отфильтровать DataFrame, чтобы в нем остались только мужчины старше 50 лет
# или женщины младше 30 лет. Функция должна вернуть отфильтрованный DataFrame в формате JSON.
#
# import pandas as pd
#
# df = pd.read_csv('titanic.csv')
#
# def titanic_list(df):
#     men_50 = (df['Sex'] == 'male') & (df['Age'] >= 50)
#     women_30 = (df['Sex'] == 'female') & (df['Age'] <= 30)
#     result_filter = df[men_50 | women_30]
#     return result_filter
#
# result = titanic_list(df)
# result_titanic = result.to_json('titanic_2.json')


# Напишите функцию, которая вычислит среднюю стоимость билета на пассажира для каждого класса.
# Функция принимает датафрейм и должна вернуть результат в виде словаря в формате JSON.

import pandas as pd

df = pd.read_csv('titanoc.csv')


def titanic_avg(df):

