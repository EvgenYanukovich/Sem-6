def is_prime(n):
    if n < 2:
        return False
    for i in range(2, s + 1):
        if n % i == 0:
            return False
    return True

def check_number(number):
    characteristics = []
    
    if number % 2 == 0:
        characteristics.append("чётное")
    else:
        characteristics.append("нечётное")
    
    if is_prime(number):
        characteristics.append("простое")
    else:
        characteristics.append("составное")
    
    return characteristics

print("Введите целое число:")
try:
    number = int(input())
    characteristics = check_number(number)
    print(f"\nЧисло {number} является:")
    for characteristic in characteristics:
        print(f"- {characteristic}")
        
except ValueError:
    print("Ошибка: Введите корректное целое число")




