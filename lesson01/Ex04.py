num = int(input('Введите целое положительное число: '))

cur_digit = 0
max = 0

while num:
    cur_digit = num - num // 10 * 10
    if cur_digit > max:
        max = cur_digit
    num = num // 10

print(f'Максимальная цифра в числе - {max}')

