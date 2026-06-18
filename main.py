import csv

books = [
    {"title": "Мастер и Маргарита", "author": "Булгаков", "year": 1967, "rating": 4.8},
    {"title": "Преступление и наказание", "author": "Достоевский", "year": 1866, "rating": 4.7},
    {"title": "Война и мир", "author": "Толстой", "year": 1869, "rating": 4.6},
    {"title": "Маленький принц", "author": "Экзюпери", "year": 1943, "rating": 4.5},
]



with open('books.csv', 'w', newline='', encoding='UTF-8') as file:
    fieldnames = ['title', 'author', 'year', 'rating']
    write = csv.DictWriter(file, fieldnames=fieldnames)
    write.writeheader()
    write.writerows(books)

