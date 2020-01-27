class Stationery():
    title = 'Name'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки ручкой.')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки карандашом.')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки Маркером.')


red_pen = Pen()
red_pen.draw()
print(red_pen.title)


wood_pencil = Pencil()
wood_pencil.draw()

black_handle = Handle()
black_handle.draw()