import math

data = input("Введите: число1 знак число2 (например: 5 + 3): ").split()

a = float(data[0])
op = data[1]
b = float(data[2])

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b if b != 0 else "на ноль делить нельзя"
elif op == "%":
    result = a % b
elif op == "//":
    result = a // b
elif op == "**":
    result = a ** b
elif op == "%%":
    result = a * b / 100       # b процентов от a
elif op == "/**":
    result = math.sqrt(a)      # корень из первого числа
else:
    result = "Неизвестная операция"

print(f"{a} {op} {b} = {result}")