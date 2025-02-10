# Пример интернирования строк
str1 = 'python'
str2 = 'python'
str3 = 'Python'

print("Интернирование строк:")
print(f"str1 = 'python'")
print(f"str2 = 'python'")
print(f"str3 = 'Python'")
print(f"str1 is str2: {str1 is str2}")  # True - строки интернированы
print(f"str1 is str3: {str1 is str3}")  # False - разные строки

# Пример интернирования чисел
num1 = 42
num2 = 42
num3 = 257
num4 = 257

print("\nИнтернирование чисел:")
print(f"num1 = 42")
print(f"num2 = 42")
print(f"num1 is num2: {num1 is num2}")  # True - числа в диапазоне -5 до 256 интернируются

print(f"\nnum3 = 257")
print(f"num4 = 257")
print(f"num3 is num4: {num3 is num4}")  # False - числа вне диапазона интернирования
