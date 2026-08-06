# import csv
# import psycopg2
#
#
# def fill_table_for_csv(table_name, file_name):
#
#     with psycopg2.connect(
#         host='localhost',
#         user='postgres',
#         dbname='courses',
#         password='515467',
#         port='5432'
#     ) as conn:
#         with conn.cursor() as cur:
#
#
#             with open(file_name, 'r', encoding='utf-8') as file:
#                 rows = csv.reader(file)
#                 headers = next(rows)
#
#                 for row in rows:
#                     query = f'INSERT INTO {table_name} ({", ".join(headers)}) VALUES ({", ".join(["%s"] * len(row))})'
#                     cur.execute(query, row)
#
#             conn.commit()
#
# def main():
#     fill_table_for_csv('students', 'data/students.csv')
#     fill_table_for_csv('instructors', 'data/instructors.csv')
#     fill_table_for_csv('courses', 'data/courses.csv')
#
#
# if __name__ == '__main__':
#     main()

сur.execute(f'CREATE TABLE customers (customer_id CHAR(5) NOT NULL, company_name CHAR(100) NOT NULL, contact_name CHAR(100) NOT NULL))'



