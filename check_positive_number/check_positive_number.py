# Создаем класс NegativeNumberError, наследующий от Exception

class NegativeNumberError(Exception):
    def __init__(self, value,message="Число не должно быть отрицательным"):
        self.value = value
        self.message = message
        super().__init__(self.message)
        
    def __str__(self):
        return f"{self.message}: {self.value}"
    
# Функция для проверки, является ли число положительным
def check_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    print(f"{number} является положительным числом")

# Проверка функции с различными значениями
try:
    check_positive_number(-5)  # Отрицательное число
except NegativeNumberError as e:
    print(e)

try:
    check_positive_number(10)  # Положительное число
except NegativeNumberError as e:
    print(e)
    