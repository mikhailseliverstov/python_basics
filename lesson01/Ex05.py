viruchka = int(input('Введите выручку: '))
rashodi = int(input('Введите расходы: '))

pribyl = viruchka-rashodi

if pribyl > 0:
    print('Ваша фирма прибыльна')
    print(f'Рентабельность - {pribyl/viruchka*100}%')
    employes = int(input('Введите количество сотрудников: '))
    print(f'Прибыль на одного сотрудника составляет {pribyl/employes}')
elif pribyl == 0:
    print('Ваша фирма работает в ноль')
else:
    print('Ваша фирма убыточна')