symbol = input("Символ: ")
height = int(input("Высота: "))
width = int(input("Ширина: "))

row = 0
while row < height:
    line = ""
    col = 0
    while col < width:
        # Рамка: первая/последняя строка ИЛИ первый/последний столбец
        if row == 0 or row == height - 1 or col == 0 or col == width - 1:
            line += symbol
        else:
            line += " "
        col += 1
    print(line)
    row += 1