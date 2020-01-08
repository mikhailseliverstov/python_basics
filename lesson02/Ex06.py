cycle = 'y'
num = 0
item_list = list()

while cycle != 'n':
    num += 1
    item_name = input('Введите название товара: ')
    item_price = input('Введите цену товара: ')
    item_count = input('Введите количество товара: ')
    item_dimension = input('Введите размерность товара: ')
    item = (num, {'Название': item_name, 'Цена': item_price, 'Количество': item_count, 'ед': item_dimension})
    print(item)
    item_list.append(item)
    print('\n')
    cycle = input('ВВЕСТИ ЕЩЁ ОДИН ТОВАР? y/n: ')
    print('\n')

print(item_list)

# item_list = [(1, {'Название': 'Мышь', 'Цена': '500', 'Количество': '15', 'ед': 'шт'}), (2, {'Название': 'Кот', 'Цена': '10000', 'Количество': '2', 'ед': 'шт'}), (3, {'Название': 'Лом', 'Цена': '700', 'Количество': '4', 'ед': 'шт'}), (4, {'Название': 'Молоко', 'Цена': '50', 'Количество': '8', 'ед': 'литр'})]
# print(item_list)
itmnm = list()
ind = -1
analytics = dict()
for y in range(len(item_list[0][1])): #цикл по количеству ключей в словаре
    ind += 1 #индекс для перебора ключей в словаре
    itmnm = list() #временный список для сбора значений ключей
    for i in item_list: #цикл по количеству товаров в списке
        q = i[1] #выделяем словарь
        keys = list(q.keys()) #переводим ключи из словаря в список для индексирования
        itmnm.append(i[1].get(keys[ind])) #достаём значение ключа и добавляем его в список
        an = {keys[ind]: itmnm} #складываем ключ и список со значениями во временный словарь
        analytics.update(an) #дописываем в словарь ключи и значения

print(analytics)
