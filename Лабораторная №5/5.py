import random
import string


def generate_random_string(length: int) -> str:
    """Генерирует случайную строку из букв ASCII и цифр."""
    characters = string.ascii_letters + string.digits + string.punctuation + ' '
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


message = input("Введите сообщение: ")
n = int(input("Введите количество подстановочных символов: "))

encoded = ""
for ch in message:
    encoded += ch + generate_random_string(n)

print("Закодированное послание:")
print(encoded)