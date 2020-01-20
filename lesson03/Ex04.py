num = input('Число. Введите действительное положительное число: ')
deg = input('Степень. Введите целое отрицательное число: ')

def my_func(x, y):
    try:
        if float(x) > 0:
            try:
                if int(y) < 0 and int(y) % 1 == 0:
                    print(f"Решение без цикла {x} в степени {y} = {float(x)**int(y)}")
                    num1 = 1
                    for i in range(1, abs(int(deg))+1):
                        num1 = num1 * (1/int(num))
                    print(f"Решение с циклом {x} в степени {y} = {num1}")
                else:
                    print('Степень должна быть целым отрицательным числом')
            except ValueError:
                print('Степень должна быть числом')
        else:
            print('Число должно быть положительным числом')
    except ValueError:
        print('Число должно быть положительным числом')

my_func(num, deg)
