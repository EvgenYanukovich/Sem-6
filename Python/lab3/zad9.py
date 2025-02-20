import re

def check_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d).{8,}$'
    if re.match(pattern, password):
        return "Пароль соответствует требованиям"
    return "Пароль не соответствует требованиям"

def check_phone_number(phone):
    pattern = r'^\(\d{3}\) \d{3}-\d{4}$'
    if re.match(pattern, phone):
        return "Номер телефона соответствует формату"
    return "Invalid Number"

def check_date(date):
    pattern = r'^(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-\d{4}$'
    if not re.match(pattern, date):
        return "Invalid Date"
    
    day, month, year = map(int, date.split('-'))
    days_in_month = {
        1: 31, 2: 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28,
        3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if day > days_in_month[month]:
        return "Invalid Date"
    
    return "Дата корректна"

if __name__ == "__main__":
    print("\nПроверка пароля:")
    password = input("Введите пароль: ")
    print(check_password(password))
    
    print("\nПроверка номера телефона:")
    phone = input("Введите номер телефона в формате (XXX) XXX-XXXX: ")
    print(check_phone_number(phone))
    
    print("\nПроверка даты:")
    date = input("Введите дату в формате DD-MM-YYYY: ")
    print(check_date(date))