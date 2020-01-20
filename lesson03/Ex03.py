def my_func(arg1, arg2, arg3):
    try:
        print(float(arg1) + float(arg2) + float(arg3) - min(float(arg1), float(arg2), float(arg3)))
    except TypeError:
        print('Ошибка. Введите три числа')
    except ValueError:
        print('Ошибка. Введите три числа')

numbers = input('Input 3 numbers: ').split()

my_func(numbers[0], numbers[1], numbers[2])

