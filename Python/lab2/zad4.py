# Лабораторная работа №2
# Вариант 14
# Выполнил: Янукович Евгений Дмитриевич

def find_divisors(N, M):
    """Находит все числа от 1 до N, которые являются делителями числа M"""
    divisors = []
    i = 1
    
    while i <= N:
        # Пропускаем отрицательные числа и ноль
        if M == 0:
            break
            
        # Проверяем, является ли число делителем
        if M % i == 0:
            divisors.append(i)
            
        # Если i превысило N, прерываем цикл
        if i > N:
            break
            
        i += 1
        
    return divisors

# Получение чисел N и M от пользователя
print("Введите число N (верхняя граница поиска делителей):")
try:
    N = int(input())
    print("Введите число M (число, для которого ищем делители):")
    M = int(input())
    
    if N < 1:
        print("N должно быть положительным числом")
    else:
        divisors = find_divisors(N, M)
        if divisors:
            print(f"\nДелители числа {M} от 1 до {N}:")
            print(", ".join(map(str, divisors)))
            print(f"Всего найдено делителей: {len(divisors)}")
        else:
            print(f"В диапазоне от 1 до {N} не найдено делителей числа {M}")
            
except ValueError:
    print("Ошибка: Введите корректные целые числа")
