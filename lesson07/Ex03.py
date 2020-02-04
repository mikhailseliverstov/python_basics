class Cell:
    def __init__(self, p1):
        self.p1 = p1

    def __add__(self, other):
        summa = self.p1 + other.p1
        return summa

    def __sub__(self, other):
        if self.p1 > other.p1:
            raznost = self.p1 - other.p1
        else:
            raznost = "Нельзя вычитать из меньшей клетки бОльшую"
        return raznost


    def __mul__(self, other):
        proizv = self.p1 * other.p1
        return proizv

    def __truediv__(self, other):
        chastnoe = round(self.p1 / other.p1)
        return chastnoe

    def __str__(self):
        return self.p1

    def make_order(self, x):
        ryad = ""
        for i in range(1,self.p1+1):
            ryad = ryad + '*' if i % x != 0 else ryad + "*\n"
        print(ryad)



c1 = Cell(24)
c2 = Cell(30)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

c1.make_order(5)
c2.make_order(9)
