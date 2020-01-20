def div(arg1, arg2):
    try:
        print(arg1 / arg2)
    except ZeroDivisionError:
        print('Ошибка деления на ноль')
    except TypeError:
        print('Нужно ввести числа')
    except ValueError:
        print('Нужно ввести числа')

args = input('Введите делимое и делитель через пробел: ').split()
arg1 = float(args[0])
arg2 = float(args[1])

div(arg1, arg2)