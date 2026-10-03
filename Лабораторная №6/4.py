text = input("Введите текст: ")
start, end = map(int, input("Введите начало и конец через пробел: ").split())

# -1, потому что пользователь считает с 1, а Python — с 0.
# end без -1, потому что конец включается.
result = text[start - 1:end]

print(result)