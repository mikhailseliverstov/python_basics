def salary_stat():
    with open('Ex03.txt') as f:
        empl_l = [st.split() for st in f]
        empl_d = {empl_l[num][0]: empl_l[num][1] for num, el in enumerate(empl_l)}
        print(f'Все сотрудники: {empl_d}')
        print(f"Сотрудники с зп ниже 20к: ", {el for el in empl_d if empl_d[el] < '20000'})
        print(f"Средняя зп: {sum(map(int,[empl_d[el] for el in empl_d]))/len(empl_l)}")

salary_stat()