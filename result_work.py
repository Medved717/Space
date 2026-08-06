# Исходные данные для заполнения таблиц
import csv
import psycopg2

# Чтение customers_data
with open('customers_data.csv', newline='') as file:
    header_customers = next(csv.reader(file))
    customers_data = [row for row in csv.reader(file) if 'customer_id' not in row]

# Чтение employees_data (универсальный способ)
with open('employees_data.csv', newline='') as file:
    # Пробуем определить разделитель автоматически
    sample = file.read(1024)
    file.seek(0)

    if '\t' in sample:
        delimiter = '\t'
    else:
        delimiter = ','

    reader = csv.reader(file, delimiter=delimiter)

    # Читаем заголовки
    try:
        headers = next(reader)
    except StopIteration:
        headers = []

    # Проверяем, есть ли employee_id в заголовках
    if 'employee_id' not in headers:
        # Если нет - добавляем сами
        header_employees = ['employee_id', 'first_name', 'last_name', 'title', 'birth_date', 'notes']
        employees_data = []
        for employee_id, row in enumerate(reader, start=1):
            if row and any(row):
                # Если в строке 5 элементов, добавляем ID
                if len(row) == 5:
                    employees_data.append([str(employee_id)] + row)
                else:
                    employees_data.append(row)
    else:
        # Если есть - используем как есть
        header_employees = headers
        employees_data = [row for row in reader]

# Чтение orders_data
with open('orders_data.csv', newline='') as file:
    header_orders = next(csv.reader(file))
    orders_data = [row for row in csv.reader(file) if 'order_id' not in row]

# Подключение к БД
conn = psycopg2.connect(
    host='sql_db',
    port='5432',
    dbname='analysis',
    user='simple',
    password='qweasd963'
)

cur = conn.cursor()

cur.execute("create schema if not exists itresume19259;")
cur.execute("SET search_path TO itresume19259;")
cur.execute("DROP TABLE IF EXISTS orders")
cur.execute("DROP TABLE IF EXISTS customers")
cur.execute("DROP TABLE IF EXISTS employees")

# Создание таблиц (исправлено: CHAR → VARCHAR)
cur.execute(
    'CREATE TABLE customers (customer_id CHAR(5) PRIMARY KEY, company_name VARCHAR(100) NOT NULL, contact_name VARCHAR(100) NOT NULL)')
cur.execute(
    'CREATE TABLE employees (employee_id INT PRIMARY KEY, first_name VARCHAR(25) NOT NULL, last_name VARCHAR(35) NOT NULL, title VARCHAR(100) NOT NULL, birth_date DATE NOT NULL, notes TEXT)')
cur.execute('''
    CREATE TABLE orders (
        order_id INT NOT NULL,
        customer_id CHAR(5) NOT NULL,
        employee_id INT NOT NULL,
        order_date DATE NOT NULL,
        ship_city VARCHAR(100) NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
    )
''')

conn.commit()

# Вставка customers
for row in customers_data:
    query = f'INSERT INTO customers ({", ".join(header_customers)}) VALUES ({", ".join(["%s"] * len(row))}) RETURNING *'
    cur.execute(query, row)

conn.commit()
res_customers = cur.fetchall()

# Вставка employees
for row in employees_data:
    query = f'INSERT INTO employees ({", ".join(header_employees)}) VALUES ({", ".join(["%s"] * len(row))}) RETURNING *'
    cur.execute(query, row)

conn.commit()
res_employees = cur.fetchall()

# Вставка orders
for row in orders_data:
    query = f'INSERT INTO orders ({", ".join(header_orders)}) VALUES ({", ".join(["%s"] * len(row))}) RETURNING *'
    cur.execute(query, row)

conn.commit()
res_orders = cur.fetchall()

cur.close()
conn.close()

print(res_customers)
print(res_employees)
print(res_orders)