# my_list = [1, 2, 3, 4, 5, 6, 7]
my_list = list(input('Введите элементы списка без пробелов: '))

for el in my_list:
    cur_ind = my_list.index(el)  # помещаем текущий индекс в переменную
    prev_ind = my_list.index(el) - 1  # помещаем предыдущий индекс в переменную
    if my_list.index(el) % 2 != 0:  # шагаем по нечётным индексам
        my_list[prev_ind] = el  # заменяем предыдущий элемент текущим
        my_list[cur_ind] = previous_el  # заменяем текущий элемент предыдущим
    previous_el = el  # запоминам текущий элемент как предыдущий

print(my_list)