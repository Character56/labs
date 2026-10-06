count = 0

while True:
    number = int(input("Введите число (0 — стоп): "))
    if number == 0:
        break
    count += 1

print("Количество введённых чисел:", count)