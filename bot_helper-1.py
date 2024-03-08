def input_error(func):
    # Декоратор для обробки помилок введення користувача
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command. Please provide username."

    return inner

@input_error
def add_contact(args, contacts):
    # Функція для додавання нового контакту
    # Перевірка чи користувач передав два аргументи: ім'я та номер телефону
    if len(args) != 2:
        return "Invalid command. Please provide username and phone number separated by space."
    username, phone = args
    # Додаємо новий контакт до словника контактів
    contacts[username] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    # Функція для зміни номера телефону контакту
    if len(args) != 2:
        return "Invalid command. Please provide username and new phone number separated by space."
    username, new_phone = args
    # Перевірка, чи ім'я користувача існує у словнику контактів
    if username not in contacts:
        return "Contact not found."
    contacts[username] = new_phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    # Функція для відображення номера телефону контакту
    if len(args) != 1:
        return "Invalid command. Please provide username."
    username = args[0]
    if username not in contacts:
        return "Contact not found."
    return contacts[username]

@input_error
def show_all(contacts):
    # Функція для відображення усіх контактів
    if not contacts:
        return "No contacts found."
    result = "\n".join([f"{username}: {phone}" for username, phone in contacts.items()])
    return result

def parse_input(user_input):
    # Функція для розбиття введеного рядка на команду та аргументи
    # Розділяємо введений рядок на команду та аргументи
    cmd, *args = user_input.split()
    # Перетворення команди до нижнього регістру
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        # Очікуємо введення команди користувачем
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        # Перевіряє, чи введена команда є однією з команд завершення роботи
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # Відповідаємо на команди
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
