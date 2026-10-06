phone_book = {
    "Иван": "+7-900-123-45-67",
    "Анна": "+7-900-765-43-21",
    "Пётр": "+7-900-111-22-33"
}

while True:
    print("\nМеню:")
    print("1 - Показать все контакты")
    print("2 - Добавить контакт")
    print("3 - Удалить контакт")
    print("4 - Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        print("\nКонтакты:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")

    elif choice == "2":
        name = input("Введите имя: ")
        if name in phone_book:
            print("Контакт с таким именем уже есть")
        else:
            phone = input("Введите телефон: ")
            phone_book[name] = phone
            print("Контакт добавлен")

    elif choice == "3":
        name = input("Введите имя для удаления: ")
        if name in phone_book:
            del phone_book[name]
            print("Контакт удалён")
        else:
            print("Такого контакта не существует")

    elif choice == "4":
        print("До свидания!")
        exit()

    else:
        print("Неверный выбор")