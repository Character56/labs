text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

count = text.count(word)

if count > 0:
    first_index = text.find(word)
    print("Количество вхождений:", count)
    print("Индекс первого вхождения:", first_index)
else:
    print("Слово не найдено")

cleaned = text.replace(word, "")
print("Текст без слова:")
print(cleaned)