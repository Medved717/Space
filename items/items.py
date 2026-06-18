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
#
#
# grades = {
#     'Анна': {'Математика': 5, 'Физика': 4, 'Химия': 5},
#     'Борис': {'Математика': 3, 'Физика': 4, 'Химия': 3},
#     'Виктор': {'Математика': 5, 'Физика': 5, 'Химия': 4},
#     'Галина': {'Математика': 4, 'Физика': 4, 'Химия': 5}
# }
#
# mark_sred = float(4.5)
# students = {}
#
# for student, objects in grades.items():
#     student_mark = 0
#     count = 0
#     for object, mark in objects.items():
#         student_mark += mark
#         count += 1
#     mark_sred_period = round(student_mark / count, 1)
#     students[student] = float(mark_sred_period)
#
# best_students = {}
# for student, mark in students.items():
#     if mark > 4.5:
#         best_students[student] = mark
# print(best_students)

# sales = {
#     'Понедельник': {'Яблоки': 10, 'Бананы': 5, 'Апельсины': 8},
#     'Вторник': {'Яблоки': 7, 'Бананы': 12, 'Апельсины': 3},
#     'Среда': {'Яблоки': 15, 'Бананы': 8, 'Апельсины': 10},
#     'Четверг': {'Яблоки': 6, 'Бананы': 4, 'Апельсины': 9},
#     'Пятница': {'Яблоки': 20, 'Бананы': 10, 'Апельсины': 5}
# }
#
# all_quantity_sales = {}
#
#
# for day, fruits in sales.items():
#     for fruit, sale in fruits.items():
#         if fruit not in all_quantity_sales:
#             all_quantity_sales[fruit] = sale
#         else:
#             all_quantity_sales[fruit] += int(sale)
#
#
# print (f' Победителем по продажам стал {max(all_quantity_sales)} с результатам {all_quantity_sales[max(all_quantity_sales)]}'
#        f'со средним показателем за день {all_quantity_sales[max(all_quantity_sales)]/len(sales)}')


employees = {
    'Иван': {'отдел': 'IT', 'зарплата': 120000, 'стаж': 3},
    'Мария': {'отдел': 'HR', 'зарплата': 85000, 'стаж': 5},
    'Петр': {'отдел': 'IT', 'зарплата': 150000, 'стаж': 7},
    'Анна': {'отдел': 'Финансы', 'зарплата': 95000, 'стаж': 4},
    'Сергей': {'отдел': 'IT', 'зарплата': 110000, 'стаж': 2},
    'Елена': {'отдел': 'HR', 'зарплата': 90000, 'стаж': 6}
}

# max_zp = max(employees, key=lambda name: employees[name]['зарплата'])
# employees_1 = employees[max_zp]['зарплата']
# print(max_zp, employees_1)
employees_1 = max(employees, key=employees.get)
