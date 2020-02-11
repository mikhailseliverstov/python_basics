from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def square(self):
        pass


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.param = param
        self.com_s = self.param / 6.5 + 0.5

    @property
    def square(self):
        s = self.param / 6.5 + 0.5
        return s


class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)
        self.param = param
        self.com_s = self.param * 2 + 0.3

    @property
    def square(self):
        s = self.param * 2 + 0.3
        return s


class Material:
    def __init__(self):
        self.com_s = []

    def coat_s(self, param):
        self.com_s.append(Coat(param))

    def suit_s(self, param):
        self.com_s.append(Suit(param))

    def common_square(self):
        com_sq = 0
        for el in self.com_s:
            com_sq += el.com_s
        return com_sq


coat = Coat(52)
suit = Suit(1.80)
print(coat.square)
print(suit.square)
m = Material()
m.coat_s(52)
m.suit_s(1.8)
print(m.common_square())