def find_pairs(N, M):
    pairs = []
    
    for i in range(1, N + 1):
        for j in range(i, N + 1): 
            if i + j <= M:
                pairs.append((i, j))
            else:
                break 
                
    return pairs

print("Введите число N (верхняя граница для пар чисел):")
try:
    N = int(input())
    print("Введите число M (максимальная сумма пары):")
    M = int(input())
    
    if N < 1:
        print("N должно быть положительным числом")
    else:
        pairs = find_pairs(N, M)
        if pairs:
            print(f"\nНайденные пары чисел, сумма которых не превышает {M}:")
            for i, (a, b) in enumerate(pairs, 1):
                print(f"{i}. ({a}, {b}) = {a + b}")
            print(f"\nВсего найдено пар: {len(pairs)}")
        else:
            print(f"Не найдено пар чисел от 1 до {N}, сумма которых не превышает {M}")
            
except ValueError:
    print("Ошибка: Введите корректные целые числа")
