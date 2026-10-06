from random import randint

secret = randint(1, 100)
attempts = 0

while True:
    guess = int(input("Угадайте число от 1 до 100: "))
    attempts += 1

    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        print("Угадал!")
        print("Попыток:", attempts)
        break