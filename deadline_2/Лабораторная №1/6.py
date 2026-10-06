symbol = input("Символ: ")
height = int(input("Высота: "))
width = int(input("Ширина: "))

row = 0
while row < height:
    line = ""
    col = 0
    while col < width:
        line += symbol
        col += 1
    print(line)
    row += 1