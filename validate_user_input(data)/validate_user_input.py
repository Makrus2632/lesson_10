def validate_user_input(data):
    # Проверка, что data является словарем
    if not isinstance(data, dict):
        raise TypeError("Ожидался словарь с данными пользователя") from None
    
    # Проверка наличия и типа ключа 'name'
    if "name" not in data or not isinstance(data["name"], str):
        raise ValueError("Ключ 'name' должен быть строкой и присутствовать в данных") from None
    
    # Проверка наличия и значения ключа 'age'
    if "age" not in data or not isinstance(data["age"], (int, float)) or data["age"] <= 0:
        raise ValueError("Ключ 'age' должен быть положительным числом и присутствовать в данных") from None

    print("Данные пользователя корректны")

# Проверка функции с различными входными данными
try:
    validate_user_input({"name": "Alice", "age": 30})  # Корректные данные
except Exception as e:
    print(e)

try:
    validate_user_input({"name": "Alice"})  # Отсутствует ключ 'age'
except Exception as e:
    print(e)

try:
    validate_user_input({"name": 123, "age": 30})  # Некорректное значение 'name'
except Exception as e:
    print(e)

try:
    validate_user_input({"name": "Alice", "age": -5})  # Некорректное значение 'age'
except Exception as e:
    print(e)

try:
    validate_user_input("Alice")  # Некорректный тип данных (строка вместо словаря)
except Exception as e:
    print(e)
