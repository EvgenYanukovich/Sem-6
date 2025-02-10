import math

# Запрос угла в градусах
print("Введите угол в градусах:")
degrees = float(input())

# Преобразование в радианы
radians = math.radians(degrees)

# Вычисление синуса и косинуса
sin_value = math.sin(radians)
cos_value = math.cos(radians)

# Вывод результатов
print(f"\nУгол {degrees}° в радианах: {radians:.4f}")
print(f"Синус угла {degrees}°: {sin_value:.4f}")
print(f"Косинус угла {degrees}°: {cos_value:.4f}")
