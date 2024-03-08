class Field:
    # Базовий клас для полів запису
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Клас для зберігання імені контакту. Обов'язкове поле.
    pass

class Phone(Field):
    # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits long.")
        super().__init__(value)

class Record:
    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Додавання телефону до запису
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        # Видалення телефону з запису
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        # Редагування телефону у записі
        for p in self.phones:
            if str(p) == old_phone:
                p.value = new_phone

    def __str__(self):
        # Представлення запису у вигляді рядка
        phones_str = "; ".join(str(p) for p in self.phones)
        return f"Contact name: {self.name}, phones: {phones_str}"

class AddressBook:
    # Клас для зберігання та управління записами
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        # Додавання нового запису до книги контактів
        self.data[record.name.value] = record

    def delete_record(self, name):
        # Видалення запису за іменем з книги контактів
        if name in self.data:
            del self.data[name]

    def find(self, name):
        # Пошук запису за іменем
        return self.data.get(name)

    def __str__(self):
        # Представлення книги контактів у вигляді рядка
        return "\n".join(str(record) for record in self.data.values())
