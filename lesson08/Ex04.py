class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


class Sklad:
    def __init__(self):
        self.inventory = []
        self.art = 0
        self.dept = {1: 'Accounting', 2: 'Lawyer', 3: 'Marketing', 4: 'Sales'}

    def add(self, *goods):
        for item in goods:
            self.art = self.art + 1
            attributes = {'art': self.art, 'dep': 'Sklad', 'type': item.__class__.__name__}
            for attr in dir(item):
                if attr[0] != '_' and attr != 'info':
                    attributes.update({attr: getattr(item, attr)})
            self.inventory.append(attributes)

    def __str__(self):
        inv = ""
        for i in self.inventory:
            inv = inv + str(i) + '\n'
        return f"{inv}"

    def t(self):
        loop = 1
        while loop:
            self.department = input(
                '\nВведите номер отдела для передачи инвентаря\nДоступные отделы:\n1 - Accounting\n2 - Lawyers\n3 - Marketing\n4 - Sales\n')
            try:
                self.department = self.dept[int(self.department)]
            except ValueError:
                print('\nВведите ЧИСЛО соответствующее номеру отдела\n')
                continue
            except KeyError:
                print('\nВведите число СООТВЕТСТВУЮЩЕЕ номеру отдела\n')
                continue

            self.art = input(
                f"\nЧто хотим перевести в {self.department}?\nВведите артикул из доступных\n {[str(i['art']) + ' - ' + str(i['type']) + ' ' + str(i['brand']) for i in self.inventory]}\n")
            try:
                self.art = int(self.art)
            except ValueError:
                print('\nВведите число соответствующее артикулу\n')
                continue

            self.number = input(
                f"\nВведите количество передаваемых {self.inventory[self.art - 1]['type'] + ' ' + self.inventory[self.art - 1]['brand']}. На складе: {self.inventory[self.art - 1]['number']} шт.\n")
            try:
                self.number = int(self.number)
                if self.number > self.inventory[self.art - 1]['number']:
                    raise Error('Нельзя передать больше, чем есть на складе!')
                    continue
                loop = 0
            except ValueError:
                print('\nВведите число соответствующее количеству передаваемых единиц\n')
                continue
            except Error as err:
                print(err)

        self.inventory[self.art - 1]['number'] = self.inventory[self.art - 1]['number'] - self.number
        attributes = {}
        for attr in self.inventory[self.art - 1]:
            attributes.update({attr: self.inventory[self.art - 1][attr]})
            if attr == 'dep':
                attributes.update({'dep': self.department})
            elif attr == 'number':
                attributes.update({'number': self.number})
        self.inventory.append(attributes)
        # print(self.inventory[art-1])
        for i in self.inventory:
            print(f"{i}")
        print('\n')


class Orgtehnika:
    def __init__(self, brand, price, number):
        self.brand = brand
        self.price = price
        self.number = number

    @property
    def info(self):
        print(f"\nБренд: {self.brand}\nСтоимость: {self.price} RUB\nКоличество: {self.number} шт.")


class Notebook(Orgtehnika):
    def __init__(self, brand, price, number, weight):
        super().__init__(brand, price, number)
        self.weight = weight

    @property
    def info(self):
        print(
            f"\nНоутбук\nБренд: {self.brand}\nСтоимость: {self.price} RUB\nКоличество: {self.number} шт.\nВес: {self.weight}")


class Printer(Orgtehnika):
    def __init__(self, brand, price, number, color):
        super().__init__(brand, price, number)
        self.color = color

    @property
    def info(self):
        print(
            f"\nПринтер\nБренд: {self.brand}\nСтоимость: {self.price} RUB\nКоличество: {self.number} шт.\nЦветной: {self.color_type}")


class Monitor(Orgtehnika):
    def __init__(self, brand, price, number, screen):
        super().__init__(brand, price, number)
        self.screen = screen

    @property
    def info(self):
        print(
            f"\nМонитор\nБренд: {self.brand}\nСтоимость: {self.price} RUB\nКоличество: {self.number} шт.\nДиагональ: {self.screen}")


n1 = Notebook("Lenovo", 100000, 3, 1050)
n2 = Notebook("ASUS", 60000, 10, 2100)
p1 = Printer("Brother", 5300, 6, False)
p2 = Printer("HP", 5300, 6, True)
m1 = Monitor("Samsung", 18000, 12, 24)
m2 = Monitor("Acer", 13000, 15, 21)

s = Sklad()
s.add(n1, n2, p1, p2, m1, m2)
print(s)
stop = 1

while stop:
    print('=====================================\n'
          'Вас приветствует программа Склад 1.0'
          '\n=====================================')
    command = input('Введите команду:\nt - для перевода инвентаря со склада в другой отдел\n0 - для выхода\n')
    if command == '0':
        break
    try:
        eval(f's.{command}()')
    except AttributeError:
        print('Выберите команду из доступных')
        continue
