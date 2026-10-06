text = input("Введите строку: ").lower()

char_counts = {}
for ch in text:
    if ch in char_counts:
        char_counts[ch] += 1
    else:
        char_counts[ch] = 1

print(char_counts)