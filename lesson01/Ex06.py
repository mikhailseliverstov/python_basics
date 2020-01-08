first = int(input('Введите первый результат: '))
plan = int(input('Введите желаемый результат: '))

day = 1
dist = first
while True:
    if plan < dist:
        print(f'На {day} день')
        break
    day += 1
    dist = dist*1.1