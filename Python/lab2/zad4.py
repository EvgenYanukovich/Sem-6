def find_divisors(N, M):
    divisors = []
    i = 1
    
    while i <= N:
        if M == 0:
            break
        
        if M % i == 0:
            divisors.append(i)
        
        if i > N:
            break
            
        i += 1
        
    return divisors

try:
    N = int(input("Введите число N (верхняя граница поиска делителей): "))
    M = int(input("Введите число M (число, для которого ищем делители): "))
    
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
