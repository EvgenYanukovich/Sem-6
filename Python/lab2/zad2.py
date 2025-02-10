# Лабораторная работа №2
# Вариант 14
# Выполнил: Янукович Евгений Дмитриевич

def classify_day(day):
    """Классифицирует день месяца по декадам"""
    match day:
        case _ if 1 <= day <= 10:
            return "Первая декада"
        case _ if 11 <= day <= 20:
            return "Вторая декада"
        case _ if 21 <= day <= 31:
            return "Третья декада"
        case _:
            return "Некорректный день месяца"

# Получение дня от пользователя
print("Введите день месяца (1-31):")
try:
    day = int(input())
    result = classify_day(day)
    print(f"\nРезультат: {result}")
except ValueError:
    print("Ошибка: Введите корректное целое число")
