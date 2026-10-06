print("Введите текст (пустая строка — конец ввода):")

word_stats = {}

while True:
    line = input()
    if line == "":
        break
    # Разбиваем строку на слова, убираем знаки препинания
    for word in line.split():
        clean = ""
        for ch in word:
            if ch.isalpha():
                clean += ch
        if clean:
            clean = clean.lower()
            if clean in word_stats:
                word_stats[clean] += 1
            else:
                word_stats[clean] = 1

print("Статистика слов:", word_stats)