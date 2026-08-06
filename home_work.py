# Исходные данные для заполнения таблиц
import csv
import psycopg2

with open('customers_data.csv', newline='') as file:
    header_customers = next(csv.reader(file))
    customers_data = [row for row in csv.reader(file) if 'customer_id' not in row]

with open('employees_data.csv', newline='') as file:
    header_employees = next(csv.reader(file))
    employees_data = [row for row in csv.reader(file) if 'first_name' not in row]

with open('orders_data.csv', newline='') as file:
    header_orders = next(csv.reader(file))
    orders_data = [row for row in csv.reader(file) if 'order_id' not in row]

# Создайте подключение к базе данных
conn = psycopg2.connect(
    host='sql_db',
    port='5432',
    dbname='analysis',
    user='simple',
    password='qweasd963'
)

# Открытие курсора
cur = conn.cursor()

# Не меняйте и не удаляйте эти строки - они нужны для проверки
cur.execute("create schema if not exists itresume19259;")
cur.execute("SET search_path TO itresume19259;")
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS customers")
cur.execute("DROP TABLE IF EXISTS employees")

# Ниже напишите код запросов для создания таблиц
cur.execute(
    f'CREATE TABLE customers (customer_id CHAR(5) PRIMARY KEY, company_name CHAR(100) NOT NULL, contact_name CHAR(100) NOT NULL)')
cur.execute(
    f'CREATE TABLE employees (employee_id INT PRIMARY KEY, first_name CHAR(25) NOT NULL, last_name  CHAR(35) NOT NULL, title CHAR(100) NOT NULL, birth_date DATE NOT NULL, notes TEXT)')
cur.execute(
    f'CREATE TABLE orders (order_id INT NOT NULL, customer_id CHAR(5) NOT NULL, employee_id INT NOT NULL, order_date DATE NOT NULL, ship_city CHAR(100) NOT NULL, FOREIGN KEY (employee_id) REFERENCES employees(employee_id), FOREIGN KEY (customer_id) REFERENCES customers(customer_id))')

# Зафиксируйте изменения в базе данных
conn.commit()

# Теперь приступаем к операциям вставок данных
# Запустите цикл по списку customers_data и выполните запрос формата
# INSERT INTO itresume3270.table (column1, column2, ...) VALUES (%s, %s, ...) returning ", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning

for row in customers_data:
    query = f'INSERT INTO itresume19259.customers ({", ".join(header_customers)}) VALUES ({", ".join(["%s"] * len(row))}) RETURNING *'
    cur.execute(query, row)

# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_customers = cur.fetchall()

# Запустите цикл по списку employees_data и выполните запрос формата
# INSERT INTO table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning *

for row in employees_data:
    query = f'INSERT INTO itresume19259.employees ({", ".join(header_employees)}) VALUES ({", ".join(["%s"] * len(row))}) RETURNING *'
    cur.execute(query, row)

# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_employees = cur.fetchall()

# Запустите цикл по списку orders_data и выполните запрос формата
# INSERT INTO table (column1, column2, ...) VALUES (%s, %s, ...) returning *", data)
# В конце каждого INSERT-запроса обязательно должен быть оператор returning *

for row in orders_data:
    query = f'INSERT INTO itresume19259.orders ({", ".join(header_orders)}) VALUES ({", ".join(["%s"] * len(row))}) RETURNING *'
    cur.execute(query, row)

# Не меняйте и не удаляйте эти строки - они нужны для проверки
conn.commit()
res_orders = cur.fetchall()

# Закрытие курсора
cur.close()

# Закрытие соединения
conn.close()