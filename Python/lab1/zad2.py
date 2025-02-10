# Создание трех числовых переменных через запятую
a, b, c = 10, 3, 7

# Вычисление различных операций
sum_result = a + b + c  # сумма
diff_result = a - b - c  # разность
mult_result = a * b * c  # произведение
mod_result = a % b  # остаток от деления
floor_div_result = a // b  # деление без остатка

# Вывод начальных значений
print(f"Начальные значения:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# Вывод результатов операций
print(f"\nРезультаты операций:")
print(f"Сумма (a + b + c): {sum_result}")
print(f"Разность (a - b - c): {diff_result}")
print(f"Произведение (a * b * c): {mult_result}")
print(f"Остаток от деления (a % b): {mod_result}")
print(f"Деление без остатка (a // b): {floor_div_result}")

# Обмен значениями переменных a и b одной строкой
a, b = b, a

# Вывод значений после обмена
print(f"\nЗначения после обмена a и b:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")