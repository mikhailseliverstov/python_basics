class Error(Exception):
    def __init(self, txt):
        self.txt = txt


a = ''
l = []
while a != 'stop':
    a = input('Введите число для добавления в список или stop для выхода: ')
    try:
        if a.replace("-","").isdigit():
            l.append(a)
        else:
            raise Error('Вы ввели не число')
    except Error as err:
        print(err)
    finally:
        print(l)
