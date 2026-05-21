import re

# Поиск всех цен в строке с использованием флагов
text = "The price of the product is $100.50"
# Флаг re.IGNORECASE не требуется в данном случае,
# но демонстрирует использование флагов
numbers = re.findall(r'\d+\.\d+', text, flags=re.IGNORECASE)
print(numbers)