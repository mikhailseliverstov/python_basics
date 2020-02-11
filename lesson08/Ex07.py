class Complex():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __str__(self):
        return f'Результат операции: {self.a} + {self.b}i'


num1 = Complex(1,3)
num2 = Complex(4,6)
print(num1 + num2)
print(num1 * num2)