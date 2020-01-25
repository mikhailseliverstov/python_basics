def file_sum():
    with open('Ex05.txt', 'w') as f:
        num = '1 2 3 4 5 6 7 8 9 10'
        f.write(num)
    with open('Ex05.txt', 'r') as f1:
        l = f1.read().split()
        print(l)
        s = sum(map(int, l))
        print(s)

file_sum()