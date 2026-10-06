text = input("Введите текст: ")

letters = 0
digits = 0
punctuation = 0
spaces = 0

punctuation_marks = ".,!?:;"

for ch in text:
    if ch.isalpha():              # буква (любая — кириллица, латиница)
        letters += 1
    elif ch.isdigit():            # цифра
        digits += 1
    elif ch in punctuation_marks: # знак препинания из списка
        punctuation += 1
    elif ch == " ":               # пробел
        spaces += 1

print("букв =", letters)
print("цифр =", digits)
print("знаков препинания =", punctuation)
print("пробелов =", spaces)