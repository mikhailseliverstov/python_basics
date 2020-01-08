my_list = []

my_list.append('string')
my_list.append(10)
my_list.append(9.9)

new_list1 = list('word')
my_list.extend(new_list1)

new_list2 = [c * 2 for c in 'list']
my_list.append(new_list2)

new_tuple = (1, 2, 3)
my_list.insert(2, new_tuple)

print(my_list)

for el in my_list:
    print(type(el))
