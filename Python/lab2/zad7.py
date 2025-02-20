def find_product_numbers(N):
    results = set() 
    
    for i in range(1, N):
        for j in range(i, N):  
            product = i * j
            if product <= N:
                results.add(product)
            else:
                break  
                
    return sorted(list(results))  

print("Введите число N:")
try:
    N = int(input())
    
    if N < 1:
        print("N должно быть положительным числом")
    else:
        numbers = find_product_numbers(N)
        if numbers:
            print(f"\nЧисла от 1 до {N}, являющиеся произведением двух чисел, меньших {N}:")
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
