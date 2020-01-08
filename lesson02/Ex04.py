string = input('Введите строку: ')

string = string.split()
counter = 0

for el in string: #enumerate(string, 1): вариант с enumerate не сработал в этом примере
    counter += 1
    print(f'{counter} {el}') if len(el) <= 10 else print(f'{counter} {el[1:10]}')
