import re

patterns = [
    re.compile(r'(\d{2})/(\d{2})/(\d{4})'),
    re.compile(r'(\d{2})-(\d{2})-(\d{4})'),
    re.compile(r'(\d{4})\.(\d{2})\.(\d{2})')
]

def normalize_date(date_str):
    for pattern in patterns:
        match = pattern.search(date_str)
        if match:
            print(match)
            # Здесь формат даты по тексту DD/MM/YYYY переходит в DD.MM.YYYY
            if pattern.pattern == r'(\d{2})/(\d{2})/(\d{4})':
                return f'{match.group(3)}.{match.group(2)}.{match.group(1)}'
            # Здесь формат даты по тексту MM-DD-YYYY переходит в DD.MM.YYYY
            if pattern.pattern == r'(\d{2})-(\d{2})-(\d{4})':
                return f'{match.group(2)}.{match.group(1)}.{match.group(3)}'
            # Здесь формат даты по тексту YYYY/MM/DD переходит в DD.MM.YYYY
            if pattern.pattern == r'(\d{4})\.(\d{2})\.(\d{2})':
                return f'{match.group(1)}.{match.group(2)}.{match.group(3)}'
    return None


def extract_and_normalize_dates(strings):
    normalized_dates = []
    for string in strings:
        normalized_date = normalize_date(string)
        if normalized_date:
            normalized_dates.append(normalized_date)
    return normalized_dates


dates = [
    "Сегодня 23/04/2021",
    "Встреча назначена на 12-05-2020",
    "Событие произошло 2019.06.17",
    "Запланировано на 07-21-2023"
]

print(extract_and_normalize_dates(dates))