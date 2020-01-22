from functools import reduce

proizv = reduce(lambda x,y: x*y, [i for i in range(100, 1001) if i % 2 == 0])

print(proizv)