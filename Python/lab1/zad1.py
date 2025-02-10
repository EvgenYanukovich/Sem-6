# Ввод значений различных типов
print("Введите целое число:")
int_var = input()
print("Введите дробное число:")
float_var = input()
print("Введите True или False:")
bool_var = input()
print("Введите строку:")
str_var = input()
print("Введите ещё одну строку:")
str_var2 = input()

# Вывод типов введенных переменных
print("\nТипы введенных переменных:")
print(f"int_var: {type(int_var)}")
print(f"float_var: {type(float_var)}")
print(f"bool_var: {type(bool_var)}")
print(f"str_var: {type(str_var)}")
print(f"str_var2: {type(str_var2)}")

# Создание переменных с явным преобразованием типов
converted_int = int(int_var)
converted_float = float(float_var)
converted_bool = bool(bool_var)
converted_str = str(123)
converted_str2 = str(3.14)

# Вывод преобразованных переменных и их типов
print("\nПреобразованные переменные и их типы:")
print(f"converted_int = {converted_int}, тип: {type(converted_int)}")
print(f"converted_float = {converted_float}, тип: {type(converted_float)}")
print(f"converted_bool = {converted_bool}, тип: {type(converted_bool)}")
print(f"converted_str = {converted_str}, тип: {type(converted_str)}")
print(f"converted_str2 = {converted_str2}, тип: {type(converted_str2)}")