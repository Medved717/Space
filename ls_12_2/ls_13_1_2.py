import logging
import os


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/ls_12_1_2.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s, %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def add(a, b):
    logger.debug('Сейчас будет производитеся сложение чисел.')
    c = a + b
    logger.info('Сложение выполнено успешно!')
    logger.info(f'Получен результат сложения {c}')
    return c


print(add(1,2))
print("Текущая директория:", os.getcwd())