def count_odd_squares(N):
    count = 0
    for i in range(1, int(N ** 0.5) + 1, 2):
        if i * i <= N:
            count += 1
    return count

print("Введите число N:")
try:
    N = int(input())
    if N < 1:
        print("Число должно быть положительным")
    else:
        result = count_odd_squares(N)
        print(f"\nКоличество чисел от 1 до {N}, являющихся квадратами нечётных чисел: {result}")
        
        print("\nЭти числа:")
        for i in range(1, int(N ** 0.5) + 1, 2):
            if i * i <= N:
                print(i * i, end=" ")
        print()  

except ValueError:
    print("Ошибка: Введите корректное целое число")
