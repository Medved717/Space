dict_categories = {
    "Супермаркеты": 76.52,
    "Аптеки": 42.03,
    "Образование": 6.87,
    "Ж/д билеты": 15.13,
    "Связь": 21.49,
    "Транспорт": 15.99,
    "Услуги банка": 2.22,
    "Наличные": 150.0,
    "Переводы": 2794.06,
    "Другое": 115.99,
    "Фастфуд": 31.63,
    "Различные товары": 14.64,
    "Рестораны": 8.63,
    "Мобильная связь": 0.8,
    "Дом и ремонт": 12.09,
    "Топливо": 5.99
}

# for key, value in dict_categories.items():
#     print(f"Категория: {key}, сумма: {value} руб.")


# max_category = None
# max_value = 0
#
# for key, value in dict_categories.items():
#     if value > max_value:
#         max_value = value
#         max_category = key
#
# print(f'Максимальная категория: {max_category}, её сумма равняется {max_value}')

# category = {}
#
# for key, value in dict_categories.items():
#     if float(value) < 10:
#         category[key] = value
#
# print(category)

#
# expenses = {
#     'Продукты': [1200, 850, 1500, 900],
#     'Транспорт': [300, 250, 400],
#     'Развлечения': [500, 700, 300, 600],
#     'Одежда': [2000, 1500],
#     'Коммунальные услуги': [3500]
# }
#
# stats = {}
#
# for key, value in expenses.items():
#     total = round(sum(value), 2)
#     average = round(sum(value) / len(value), 2)
#     count = len(value)
#     stats[key] = {'total': total, 'average': average, 'count': count}
#
# print(stats)

#
#
# sales_data = {
#     'Январь': {
#         'Анна': 15000,
#         'Борис': 22000,
#         'Виктор': 18000
#     },
#     'Февраль': {
#         'Анна': 17000,
#         'Борис': 19000,
#         'Галина': 25000
#     },
#     'Март': {
#         'Анна': 20000,
#         'Виктор': 21000,
#         'Галина': 23000
#     }
# }
#
# summary = {}
#
#
# for month, list_manager in sales_data.items():
#     for manager, price in list_manager.items():
#         if manager not in summary:
#             summary[manager] = {'total_sales': price, 'months_count': 1, 'best_month': month, 'max_sales': price}
#
#         else:
#             if summary[manager]['max_sales'] < price:
#                 summary[manager]['max_sales'] = price
#                 summary[manager]['best_month'] = month
#
#             summary[manager]['total_sales'] += price
#             summary[manager]['months_count'] += 1
#
# for manager in summary:
#     del summary[manager]['max_sales']
#
#
# print(summary)


grades = {
    'Анна': {'Математика': 5, 'Физика': 4, 'Химия': 5},
    'Борис': {'Математика': 3, 'Физика': 4, 'Химия': 3},
    'Виктор': {'Математика': 5, 'Физика': 5, 'Химия': 4},
    'Галина': {'Математика': 4, 'Физика': 4, 'Химия': 5}
}


for student, object