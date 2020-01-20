loop = 1
summa = 0
while loop:
    str = input('Введите несколько чисел разделённе пробелом: ')
    if str.find('-') > 0:
        str = str[0:str.find('-')]
        loop = 0
    #numbers = str.split()
    dgt = [int(i) for i in str.split()]
    summa = summa + sum(dgt)
    print(f'Общая сумма введённых чисел = {summa}')
print('Выход')