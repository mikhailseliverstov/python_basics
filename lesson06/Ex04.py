class Car:
    def __init__(self, speed, color, name, is_police):
        self.color = color
        self.speed = speed
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car is moving')

    def stop(self):
        print('The car is stopped')

    def turn(self, where):
        print(f'The car turned on {where}')

    def show_speed(self):
        print(f'The speed of car {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, passengers):
        super().__init__(speed, color, name, is_police)
        self.passengers = passengers

    def show_speed(self):
        if self.speed > 60:
            print(f'Attention! The speed of this car should be below 60 km/h. Current speed is {self.speed}')
        else:
            print(f'The speed of car {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, power):
        super().__init__(speed, color, name, is_police)
        self.power = power


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, axis):
        super().__init__(speed, color, name, is_police)
        self.axis = axis

    def show_speed(self):
        if self.speed > 60:
            print(f'Attention! The speed of this car should be below 40 km/h. Current speed is {self.speed}')
        else:
            print(f'The speed of car {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, type):
        super().__init__(speed, color, name, is_police)
        self.type = type


lada = TownCar(90, 'white', 'Lada', False, 4)
print(lada.speed)
print(lada.color)
print(lada.passengers)
lada.show_speed()

porsche = SportCar(150, 'Red', 'Porsche', False, 500)
print(porsche.power)
print(porsche.is_police)
porsche.show_speed()

avtozak = PoliceCar(80, 'blue', 'GAZ', True, 'furgon')
print(avtozak.is_police)
print(avtozak.type)

delivery = WorkCar(75, 'grey', 'Gazel', False, 2)
print(delivery.axis)
print(delivery.color)
delivery.show_speed()

