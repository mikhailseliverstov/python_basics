import time

class TrafficLight:
    color = ''

    def running(self):
        cnt = -1
        while True:
            col = {'Red': 3, 'Yellow': 2, 'Green': 3}
            keys = [el for el in col.keys()]
            cnt = cnt * -1
            #print(keys[1:2])
            for i in keys[::cnt]:
                if TrafficLight.color != i:
                    TrafficLight.color = i
                    print(TrafficLight.color)
                time.sleep(col.get(i))


svtfr = TrafficLight()
svtfr.running()

