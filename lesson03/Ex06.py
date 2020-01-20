str = input('Введите слово или строку из строчных прописных букв: ')
str1 = ' '

def int_func(arg):
    """Функция заменяет первую букву слова в строчную"""
    if str.replace(' ','').isalpha():
        print(arg[0].upper(), arg[1:], sep='')
        """Решения для строки из нескольких слов"""
        list1 = arg.split()
        for i in range(0, len(list1)):
            list1[i] = list1[i][0].upper() + list1[i][1:]
        print(str1.join(list1))

    else:
        print('Строка должна состоять из латинских букв')

int_func(str)
