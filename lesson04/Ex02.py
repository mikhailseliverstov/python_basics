import random
l=[]
for j in range(1,random.randint(10,30)):
    l.append(random.randint(1,j))
print(l)

l1 = [l[i] for i in range(0,len(l)) if l[i] > l[i-1]]
print(l1)