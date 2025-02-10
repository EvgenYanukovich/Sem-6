# Лабораторная работа №2
# Вариант 14
# Выполнил: Янукович Евгений Дмитриевич

import random

def guess_number():
    """Игра по угадыванию случайного числа"""
    # Генерируем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 10
    
    print("Я загадал число от 1 до 100.")
    print("У вас есть 10 попыток, чтобы угадать его.")
    
    while attempts > 0:
        print(f"\nОсталось попыток: {attempts}")
        try:
            guess = int(input("Введите ваше предположение: "))
            
            if guess < 1 or guess > 100:
                print("Число должно быть от 1 до 100!")
                continue
                
            if guess == secret_number:
                print(f"Поздравляю! Вы угадали число {secret_number}!")
                print(f"Вы справились за {10 - attempts + 1} попыток!")
                break
            elif guess < secret_number:
                print("Загаданное число больше")
            else:
                print("Загаданное число меньше")
                
            attempts -= 1
            
            if attempts == 0:
                print(f"\nИгра окончена! Загаданное число было: {secret_number}")
                
        except ValueError:
            print("Пожалуйста, введите корректное целое число!")

# Запуск игры
if __name__ == "__main__":
    print("Игра 'Угадай число'!")
    guess_number()
