import re
# Напишите программу, которая находит все даты в формате "dd-mm-yyyy" в заданном тексте.

def find_data(text):
    pettern = re.compile(r'\d\d\.\d\d\.\d\d\d\d')