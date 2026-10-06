n = int(input("Введите число n: "))

# Создаём пустую матрицу n×n
matrix = [[0] * n for _ in range(n)]

# Начинаем с центра
row = n // 2
col = n // 2
matrix[row][col] = 1

# Направления по часовой: вправо, вниз, влево, вверх
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_index = 0

num = 2
step_length = 1  # сколько шагов в текущем направлении

while num <= n * n:
    # Два прохода по каждому «кольцу»: сначала step_length, потом снова step_length
    for _ in range(2):
        dr, dc = directions[dir_index]
        for _ in range(step_length):
            row += dr
            col += dc
            if 0 <= row < n and 0 <= col < n and num <= n * n:
                matrix[row][col] = num
                num += 1
        dir_index = (dir_index + 1) % 4
    step_length += 1

# Вывод матрицы
for row in matrix:
    for value in row:
        print(f"{value:3}", end="")
    print()