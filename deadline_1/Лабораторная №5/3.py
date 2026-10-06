fio = input("Введите ФИО через пробел: ").split()

if len(fio) >= 3:
    print(fio[0].upper())  # Фамилия
    print(fio[1].upper())  # Имя
    print(fio[2].upper())  # Отчество
else:
    print("Введите Фамилию, Имя и Отчество через пробел")