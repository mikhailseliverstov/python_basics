def schedule():
    with open('Ex06.txt') as f:
        l1 = [line.split(':') for line in f]
        print(l1)
        print('\n')
        l2 = [el[1].strip() for el in l1]
        s = ''
        d = {}
        for num, i in enumerate(l2):
            qwe = 0
            l2[num] = [k for k in i if k.isdigit() or k.isspace()]
            l2[num] = s.join(l2[num]).split()
            for z in l2[num]:
                qwe = qwe + int(z)
            l2[num] = qwe

        d = {l1[num][0]: l2[num] for num in range(0, len(l2))}
        print(d)

schedule()