import csv

# with open('students.csv') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#         if float(row[2]) > 4.5:
#             print(row)


with open('students.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if float(row['avg_grade']) > 4.5:
            print(row)