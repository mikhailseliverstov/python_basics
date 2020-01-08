months_list = ('Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима')
months_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
               9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}

while True:
    number = input('Введите номер месяца: ')
    try:
        if int(number) < 13 and int(number) > 0:
            print('Решение с помощью списка:', months_list[int(number) - 1])
            print('Решение с помощью словаря:', months_dict.get(int(number)))
        else:
            print('Введено неверное значение')
            continue
    except:
        print('Введите значение от 1 до 12')
        continue
    if number.isdigit():
        number = int(number)
        break
