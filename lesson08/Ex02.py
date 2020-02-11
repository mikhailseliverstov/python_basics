class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

delitel = input('Введите число, на которое поделим 100: ')
try:
    if delitel == 0:
        raise OwnError('На ноль делить нельзя!')
    else:
        print(100 / delitel)
except:
    print('Вы ввели не число')