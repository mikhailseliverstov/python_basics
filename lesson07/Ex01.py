class Matrix():
    def __init__(self, param):
        self.param = param

    def __str__(self):
        s, s1 = " ", ""
        for i in self.param:
            s1 = s1 + s.join([str(j) for j in i]) + "\n"
        return s1

    def __add__(self, matrix2):
        matrix3 = []
        try:
            if len(self.param) == len(matrix2.param):
                strlen = len(self.param[1])
                for n, i in enumerate(self.param):
                    if strlen == len(i):
                        m3 = ([self.param[n][j] + matrix2.param[n][j] for j in range(0, len(i))])
                        matrix3.append(m3)
                    else:
                        print("Строки матрицы должны содеражть одинаковое количество элементов")
                        matrix3.clear()
                        break
            else:
                print("Матрицы должны быть одинаковой размерности")
            return Matrix(matrix3)
        except IndexError:
            print("Матрицы должны быть одинаковой размерности")

    def __str__(self):
        s, s2 = " ", ""
        for i in self.param:
            s2 = s2 + s.join([str(j) for j in i]) + "\n"
        return s2



m1 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
m2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
print(m1)
print(m2)
print(m1 + m2)
