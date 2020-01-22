import random
l=[]
for j in range(random.randint(1,5),random.randint(10,30)):
    l.append(random.randint(1,j))
print(l)
print(set(l)) #выводим множество для сравнения длины

l1 = [l[i] for i in range(0,len(l)) if l.index(l[i],i) ==  l.index(l[i])]
print(l1)