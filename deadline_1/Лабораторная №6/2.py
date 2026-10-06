text = input("Введите текст: ")
old, new = input("Введите строку1 и строку2 через пробел: ").split()

result = text.replace(old, new)

print(result)