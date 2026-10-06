fio = input("Введите ФИО через пробел: ").split()

formatted = " ".join(word.capitalize() for word in fio)

print(f"Добро пожаловать {formatted}")