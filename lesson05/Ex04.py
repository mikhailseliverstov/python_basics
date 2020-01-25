def change_lang():
    with open('Ex04.txt', 'r') as f1:
        l = [st.split(' — ') for st in f1]
        l1 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        d = {el[0]: el[1] for num, el in enumerate(l)}
        l2 = [l1.get(el)+' — '+d.get(el) for el in l1]
        with open('Ex04_1.txt', 'w') as f2:
            for i in l2:
                f2.write(i)

change_lang()
