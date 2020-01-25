import json
def data_convert():
    with open('Ex07.txt', 'r') as f1:
        l2, d, sum = [], {}, 0
        for num, line in enumerate(f1):
            l1 = line.split()
            l2.append([l1[0], int(l1[2]) - int(l1[3])])
            sum = sum + int(l1[2]) - int(l1[3]) if int(l1[2]) - int(l1[3]) > 0 else sum
        l2.append(['average_profit', sum/len(l2)])
        d = {el[0]: el[1] for el in l2}
        print(d)
        with open('Ex07_.json', 'w') as f2:
            json.dump(d, f2)

data_convert()
