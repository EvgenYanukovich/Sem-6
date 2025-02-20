a, b, c = 10, 3, 7

print(f"Начальные значения:")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

sum_result = a + b + c  
diff_result = a - b - c  
mult_result = a * b * c  
sep_result = a / b
mod_result = a % b  
floor_div_result = a // b  

print(f"\nРезультаты операций:")
print(f"Сумма (a + b + c): {sum_result}")
print(f"Разность (a - b - c): {diff_result}")
print(f"Произведение (a * b * c): {mult_result}")
print(f"Деление (a / b): {sep_result}")
print(f"Остаток от деления (a % b): {mod_result}")
print(f"Деление без остатка (a // b): {floor_div_result}")

a, b = b, a

print(f"\nЗначения после обмена a и b:")
print(f"a = {a}")
print(f"b = {b}")