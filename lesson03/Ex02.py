def pers_data(name, surname, year, city, email):
    print(f"Имя - {name}, \nФамилия - {surname}, \nГод рождения - {year}, \nГород проживания - {city}, \nEmail - {email}")

info = input('Введите через пробел имя, фамилию, год рождения, город проживания, email: ').split()

pers_data(name=info[0], surname=info[1], year=info[2], city=info[3], email=info[4])