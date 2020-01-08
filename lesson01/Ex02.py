#time_in_sec = 36000
time_in_sec = int(input('Введите время в секундах: '))

min_total = time_in_sec // 60
#print(min_total)

seconds = time_in_sec - min_total * 60
#print(seconds)

hours_total = min_total // 60
#print(hours_total)

minutes = min_total - hours_total * 60
#print(minutes)

days = hours_total // 24
#print(days)

hours = hours_total - days * 24

print(f'{days} дн. {hours//10}{hours - hours//10*10}:{minutes//10}{minutes - minutes//10*10}:{seconds//10}{seconds - seconds//10*10}')


