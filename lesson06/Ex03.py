sal = {"wage": 70000, "bonus": 20000}

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = sal


class Position(Worker):
    def get_full_name(self):
        print(f"Full employee's name: {self.name} {self.surname}")

    def get_salary(self):
        print(f"Employee's salary is {self._income['wage']+self._income['bonus']}")


storog = Position('Ivan', 'Ivanovich', 'Security')
print(f'Name: {storog.name}')
print(f'Surname: {storog.surname}')
print(f'Position: {storog.position}')
storog.get_full_name()
storog.get_salary()