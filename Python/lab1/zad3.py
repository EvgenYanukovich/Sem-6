

# Город и температура
print("Введите название города:")
city = input()
print("Введите температуру:")
temperature = float(input())
print(f"В городе {city} сейчас {temperature}°C.")

# Площадь прямоугольника
print("\nВведите длину прямоугольника:")
length = float(input())
print("Введите ширину прямоугольника:")
width = float(input())
area = length * width
print(f"Площадь прямоугольника с длиной {length} и шириной {width} равна {area}.")

# Стоимость покупки
print("\nВведите цену товара:")
price = float(input())
print("Введите количество товара:")
quantity = int(input())
total_cost = price * quantity
print(f"Итоговая стоимость {quantity} товаров по цене {price} рублей составляет {total_cost:.3f} рублей.")

# Перевод секунд
print("\nВведите время в секундах:")
total_seconds = int(input())
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"Время {total_seconds} секунд — это {minutes} минут и {seconds} секунд.")