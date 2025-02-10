# Лабораторная работа №2
# Вариант 14
# Выполнил: Янукович Евгений Дмитриевич

def find_product_numbers(N):
    """Находит все числа от 1 до N, являющиеся произведением двух чисел, меньших N"""
    results = set()  # Используем множество для исключения дубликатов
    
    # Внешний цикл для первого множителя
    for i in range(1, N):
        # Внутренний цикл для второго множителя
        for j in range(i, N):  # Начинаем с i, чтобы избежать лишних проверок
            product = i * j
            if product <= N:
                results.add(product)
            else:
                break  # Если произведение превысило N, переходим к следующему i
                
    return sorted(list(results))  # Преобразуем в отсортированный список

# Получение числа N от пользователя
print("Введите число N:")
try:
    N = int(input())
    
    if N < 1:
        print("N должно быть положительным числом")
    else:
        numbers = find_product_numbers(N)
        if numbers:
            print(f"\nЧисла от 1 до {N}, являющиеся произведением двух чисел, меньших {N}:")
            
            # Выводим числа и их множители
            for num in numbers:
                factors = []
                print(f"\n{num} можно получить как произведение:")
                for i in range(1, int(num ** 0.5) + 1):
                    if num % i == 0 and i < N and num // i < N:
                        factors.append(f"{i} × {num // i}")
                print(" или ".join(factors))
                
            print(f"\nВсего найдено чисел: {len(numbers)}")
        else:
            print(f"Не найдено подходящих чисел в диапазоне от 1 до {N}")
            
except ValueError:
    print("Ошибка: Введите корректное целое число")
