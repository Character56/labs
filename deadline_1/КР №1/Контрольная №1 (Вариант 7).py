password = input("Введите пароль: ")

# Спецсимволы, которые считаем «специальными»
specials = "!@#$%"

# Проверяем каждое условие
has_length = len(password) >= 8
has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(ch in specials for ch in password)

# Считаем, сколько условий выполнено
score = sum([has_length, has_upper and has_lower, has_digit, has_special])

# Определяем степень надёжности
if score == 4:
    strength = "Сильный"
elif score >= 2:
    strength = "Средний"
else:
    strength = "Слабый"

print(f"Надёжность пароля: {strength}")