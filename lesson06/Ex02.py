class Road():
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def massa(self):
        m = self._length * self._width * 25 * 0.05
        print(f'Massa asfalta = {int(m)} tonn')


doroga = Road(1000, 10)
doroga.massa()

