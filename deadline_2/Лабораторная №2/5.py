count = int(input("Сколько чисел вы хотите ввести? "))

numbers = []
for i in range(1, count + 1):
    num = float(input(f"Введите число {i}: "))
    numbers.append(num)

maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / len(numbers)

# Считаем, сколько чисел больше среднего
above_avg = 0
for num in numbers:
    if num > average:
        above_avg += 1

print("Результаты:")
print("Максимальное:", maximum)
print("Минимальное:", minimum)
print("Среднее:", average)
print("Чисел больше среднего:", above_avg)