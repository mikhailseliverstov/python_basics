from itertools import count, cycle

def gen():
    try:
        global l
        l = []
        num = int(input('С какого числа начать генерацию? - '))
        num1 = int(input('До какого числа генерировать? - '))
        for el in count(num):
            if el > num1:
                break
            else:
                l.append(el)
        #return l
        print(l)
    except ValueError:
        print('Для генерации списка нужно ввести число')
gen()


def repeat(list1):
    if list1 != []:
        try:
            num2 = int(input('\n Сколько раз повторить сгенерированный список? - '))
            l1 = []
            c = 1
            for i in cycle(l):
                if c > num2*len(list1):
                    break
                l1.append(i)
                c += 1
            #return l1
            print(l1)
        except ValueError:
            print('Для повторения списка нужно ввести число повторений')
        except NameError:
            print('Функции нужен список')
    else:
        print('Нечего повторять :(')
repeat(l)
