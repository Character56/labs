a, b, c = map(int, input("Введите 3 целых числа через пробел: ").split())

# Пункт 2: попарные умножения
ab = a * b
bc = b * c
ca = c * a

# Пункт 4: степень, остаток, целочисленное деление
a4 = a ** 4
rem_bc = b % c
int_div_ca = c // a if a != 0 else 0

# Пункт 6: вывод
print("a * b =", ab)
print("b * c =", bc)
print("c * a =", ca)
print("a ** 4 =", a4)
print("b % c =", rem_bc)
print("c // a =", int_div_ca)
print("Сумма промежуточных (a4 + rem_bc + int_div_ca) =", a4 + rem_bc + int_div_ca)