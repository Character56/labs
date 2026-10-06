from random import randint

# ===== НАЧАЛЬНЫЕ ДАННЫЕ =====

counter = {
    "яблоки":    {"max": 20, "current": 10},
    "бананы":    {"max": 15, "current": 8},
    "апельсины": {"max": 25, "current": 12},
    "арбузы":    {"max": 10, "current": 5},
}

store = {
    "яблоки":    {"max": 100, "current": 40},
    "бананы":    {"max": 80,  "current": 30},
    "апельсины": {"max": 120, "current": 50},
    "арбузы":    {"max": 40,  "current": 15},
}

price = {
    "яблоки":    {"sale_price": 50,  "purchase_price": 30},
    "бананы":    {"sale_price": 70,  "purchase_price": 45},
    "апельсины": {"sale_price": 60,  "purchase_price": 35},
    "арбузы":    {"sale_price": 200, "purchase_price": 150},
}

money = 2000

# ===== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ =====

def show_status():
    """Показать текущее состояние ларька."""
    print("\n" + "=" * 40)
    print(f"Деньги в кассе: {money} руб.")
    print("-" * 40)
    print("На прилавке:")
    for fruit, info in counter.items():
        print(f"  {fruit}: {info['current']} / {info['max']} (цена: {price[fruit]['sale_price']})")
    print("На складе:")
    for fruit, info in store.items():
        print(f"  {fruit}: {info['current']} / {info['max']}")
    print("=" * 40)


def restock():
    """Переложить фрукты со склада на прилавок (до максимума)."""
    print("\nПополняем прилавок со склада...")
    for fruit in counter:
        need = counter[fruit]["max"] - counter[fruit]["current"]
        if need <= 0:
            continue
        available = store[fruit]["current"]
        transfer = min(need, available)
        if transfer > 0:
            counter[fruit]["current"] += transfer
            store[fruit]["current"] -= transfer
            print(f"  {fruit}: +{transfer} (теперь на прилавке {counter[fruit]['current']})")


def sell_day():
    """Продать случайное количество фруктов за день."""
    global money
    print("\n--- Торговля ---")
    for fruit in counter:
        if counter[fruit]["current"] <= 0:
            continue
        sold = randint(0, min(3, counter[fruit]["current"]))
        if sold > 0:
            counter[fruit]["current"] -= sold
            revenue = sold * price[fruit]["sale_price"]
            money += revenue
            print(f"  Продано {sold} {fruit} за {revenue} руб.")


def change_prices():
    """Каждый день цена немного меняется (вверх или вниз)."""
    print("\n--- Изменение цен ---")
    for fruit in price:
        delta = randint(-10, 10)
        old_price = price[fruit]["sale_price"]
        new_price = max(1, old_price + delta)
        price[fruit]["sale_price"] = new_price
        if new_price != old_price:
            print(f"  {fruit}: {old_price} -> {new_price}")


def ashot_attack():
    """Ашот Похититель Арбузов: 20% шанс украсть 50-100% с прилавка."""
    if randint(1, 100) <= 20:
        print("\n!!! АШОТ ПОХИТИТЕЛЬ АРБУЗОВ АТАКУЕТ !!!")
        fruit = "арбузы"
        if counter[fruit]["current"] > 0:
            stolen_percent = randint(50, 100)
            stolen = int(counter[fruit]["current"] * stolen_percent / 100)
            counter[fruit]["current"] -= stolen
            print(f"  Ашот украл {stolen} {fruit} ({stolen_percent}%)!")
        else:
            print("  Но арбузов на прилавке не было... Ашот ушёл ни с чем.")


def buy_fruits():
    """Закупить фрукты на склад."""
    global money
    print("\n--- Закупка ---")
    for fruit in store:
        need = store[fruit]["max"] - store[fruit]["current"]
        if need <= 0:
            continue
        can_afford = money // price[fruit]["purchase_price"]
        to_buy = min(need, can_afford, 5)
        if to_buy > 0:
            cost = to_buy * price[fruit]["purchase_price"]
            store[fruit]["current"] += to_buy
            money -= cost
            print(f"  Куплено {to_buy} {fruit} за {cost} руб.")


# ===== ОСНОВНОЙ ЦИКЛ =====

print("=" * 40)
print("CRM СИСТЕМА ЛАРЬКА")
print("Проживите 10 дней и не разоритесь!")
print("=" * 40)

for day in range(1, 11):
    print(f"\n########## ДЕНЬ {day} ##########")
    show_status()

    while True:
        print("\nЧто делаем?")
        print("1 - Торговать (продать фрукты)")
        print("2 - Пополнить прилавок со склада")
        print("3 - Закупить фрукты на склад")
        print("4 - Закончить день")
        choice = input("Выбор: ")

        if choice == "1":
            sell_day()
        elif choice == "2":
            restock()
        elif choice == "3":
            buy_fruits()
        elif choice == "4":
            break
        else:
            print("Неверный выбор")

    change_prices()
    ashot_attack()

    if money <= 0:
        print("\n!!! ВЫ БАНКРОТ !!!")
        print("Придётся вернуться на арбузные плантации...")
        exit()

print("\n" + "=" * 40)
print("!!! ПОБЕДА !!!")
print("Вы прожили 10 дней! Полиция вычислила Ашота и дала ему большой срок.")
print(f"Итоговое состояние кассы: {money} руб.")
print("=" * 40)