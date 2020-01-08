my_list = [7, 5, 3, 3, 2]

rate = input('Type your rate: ')
my_str = str(my_list).replace(', ', '')  # создаём строку из списка, чтобы использовать метод rfind

if int(rate) > max(my_list):
    my_list.insert(0, int(rate)) #если введённое значение больше максимального в списке, то вставляем его первым
elif int(rate) < min(my_list):
    my_list.append(int(rate)) #если введённое значение меньше минимального в списке, то добавляем его в конец
else:
    my_list.insert(my_str.rfind(rate), int(
        rate))  # вставляем введённый рейтинг после уже существующего. Т.к. строка начинается с символа '[', то добавлять единицу к индексу не требуется

#print(my_str.rfind(rate))
#print(my_list[my_str.rfind(rate) - 1])

print(my_list)
