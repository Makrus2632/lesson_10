def convert_to_int(value):
    try:
        result = int(value)
        print(f"Успешное преобразование: {result}")
        return result
    except ValueError:
        print("Ошибка: невозможно преобразовать значение в целое число.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    finally:
        print("Попытка преобразования завершена.")

# Проверка функции с различными значениями
convert_to_int("123")      # Корректное значение, должно успешно преобразовать
convert_to_int("abc")      # Некорректное значение, вызовет ValueError
convert_to_int([1, 2, 3])  # Некорректный тип, вызовет TypeError

