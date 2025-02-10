# Лабораторная работа №2
# Вариант 14
# Выполнил: Янукович Евгений Дмитриевич

def is_prime(n):
    """Проверяет, является ли число простым"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_number(number):
    """Определяет характеристики числа"""
    characteristics = []
    
    # Проверка на четность
    if number % 2 == 0:
        characteristics.append("чётное")
    else:
        characteristics.append("нечётное")
    
    # Проверка на простое число
    if is_prime(number):
        characteristics.append("простое")
    else:
        characteristics.append("составное")
    
    return characteristics

# Получение числа от пользователя
print("Введите целое число:")
try:
    number = int(input())
    
    # Получение характеристик числа
    characteristics = check_number(number)
    
    # Вывод результата
    print(f"\nЧисло {number} является:")
    for characteristic in characteristics:
        print(f"- {characteristic}")
        
except ValueError:
    print("Ошибка: Введите корректное целое число")
