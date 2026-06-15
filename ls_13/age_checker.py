import datetime

def get_current_year() -> int:
    """
    Получает текущий год из системной даты.
    В реальности - обращение к системному времени.
    """
    return datetime.datetime.now().year


def is_adult(birth_year: int) -> bool:
    """
    Проверяет, является ли пользователь совершеннолетним (18+ лет).
    ВОТ ЭТУ ФУНКЦИЮ НУЖНО ПРОТЕСТИРОВАТЬ С МОКОМ!
    """
    current_year = get_current_year()
    age = current_year - birth_year
    return age >= 18

