number = int(input("Введите положительное целое число: "))
total = 0

while number > 0:
    digit = number % 10       # последняя цифра
    total += digit
    number = number // 10     # убираем последнюю цифру

print("Сумма цифр:", total)