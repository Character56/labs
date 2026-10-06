text = input("Введите текст: ")
word = input("Введите слово: ")

if word in text:
    print(f"Слово '{word}' найдено. Количество вхождений: {text.count(word)}")
else:
    print(f"Слово '{word}' не найдено")