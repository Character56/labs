n = int(input("Введите высоту пирамиды: "))

for i in range(1, n + 1):
    # Пробелы для отступа
    line = " " * (n - i)
    # Возрастающая часть: 1 2 ... i
    for j in range(1, i + 1):
        line += str(j)
    # Убывающая часть: i-1 ... 1
    for j in range(i - 1, 0, -1):
        line += str(j)
    print(line)