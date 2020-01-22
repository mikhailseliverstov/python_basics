#задание сделал как понял условие :)
def gnr(num):
    for i in range(1,num+1):
        yield i

f = 1

try:
    num1 = int(input('Факториал какого числа берём? - '))
    if num1 > 0:
        for j in gnr(num1):
            f = f * j
        print(f)
    else:
        print('Пожалуйста, введите натуральное число (больше 0)')
except ValueError:
    print('Пожалуйста, введите натуральное число (больше 0)')
