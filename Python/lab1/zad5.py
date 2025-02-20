from time import localtime, time, strftime

current_time = time()
local_time = localtime(current_time)

print("Текущая дата и время:", strftime("%Y-%m-%d %H:%M:%S", local_time))
print("Дата:", strftime("%d/%m/%Y", local_time))
print("Время:", strftime("%H:%M:%S", local_time))

print("\nТекущая дата и время:", strftime("%d.%m.%Y %H:%M:%S", local_time))

months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 
          'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
month_name = months[local_time.tm_mon - 1]

print(f"Дата: {local_time.tm_mday} {month_name} {local_time.tm_year}")
print(f"Время: {local_time.tm_hour:02d}:{local_time.tm_min:02d}")
