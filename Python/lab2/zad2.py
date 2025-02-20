def classify_day(day):
    match day:
        case 5 | 6 | 10:
            return "Первая декада"
        case _ if 11 <= day <= 20:
            return "Вторая декада"
        case _ if 21 <= day <= 31:
            return "Третья декада"
        case _:
            return "Некорректный день месяца"

print("Введите день месяца (1-31):")
try:
    day = int(input())
    result = classify_day(day)
    print(f"\nРезультат: {result}")
except ValueError:
    print("Ошибка: Введите корректное целое число")

