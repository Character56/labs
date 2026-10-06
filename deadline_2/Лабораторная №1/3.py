text = input("Введите строку: ")

# Убираем пробелы и приводим к нижнему регистру
cleaned = ""
i = 0
while i < len(text):
    if text[i] != " ":
        cleaned += text[i].lower()
    i += 1

# Проверяем, читается ли одинаково с двух сторон
left = 0
right = len(cleaned) - 1
is_palindrome = True

while left < right:
    if cleaned[left] != cleaned[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")