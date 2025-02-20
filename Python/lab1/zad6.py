import math

print("Введите угол в градусах:")
degrees = float(input())

radians = math.radians(degrees)

sin_value = math.sin(radians)
cos_value = math.cos(radians)

print(f"\nУгол {degrees}° в радианах: {radians:.4f}")
print(f"Синус угла {degrees}°: {sin_value:.4f}")
print(f"Косинус угла {degrees}°: {cos_value:.4f}")
