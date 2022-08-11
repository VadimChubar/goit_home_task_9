def input_error(func):
    def wrapper(user_input):
        global commands, result, contacts
        # перевірити чи номер який додається чи змінюється цифра
        if commands.get(user_input.split()[0]) in (func_add, func_change):
            try:
                user_input.split()[-1] = int(user_input.split()[-1])
            except ValueError:
                print(
                    f"Phone {user_input.split()[-1]} is not number, try again")
            else:
                result = func(user_input)

        if commands.get(user_input.split()[0]) == func_change:
            try:  # треба перевірка що словник не порожній
                contacts_check = list(contacts)[0]
            except IndexError:
                print("Phonebook is empty. Please repeat command")
            else:
                result = func(user_input)

        return result
    return wrapper


""""
parsing user input:
user_input = "add name 88888"

print(user_input.split()) # all user input 
print(user_input.split()[0])  # command
print(' '.join(user_input.split()[1:-1]))  # contact name
print(user_input.split()[-1])  # phone number
"""


@input_error
def func_add(user_input):
    global commands, contacts
    contacts[' '.join(user_input.split()[1:-1])] = user_input.split()[-1]
    return contacts


@input_error
def func_change(user_input):
    global contacts

    if contacts.get(' '.join(user_input.split()[1:-1])) is None:
        print("Contact not found. Please repeat command")
    else:
        # видаляємо контакт який треба змінити
        contacts.pop(' '.join(user_input.split()[1:-1]))
    # додаємо оновлений контакт
        contacts[' '.join(user_input.split()[1:-1])] = user_input.split()[-1]


def func_phone(user_input):
    global contacts
    if contacts.get(user_input.split()[-1]) is None:
        print("Number not found, try again")
    if contacts.get(user_input.split()[-1]) is not None:
        print(contacts.get(user_input.split()[-1]))


def func_show_all(user_input):
    global contacts
    try:  # треба перевірка що словник не порожній
        contacts_check = list(contacts)[0]
    except IndexError:
        print("Phone book is empty. Please repeat command")
    else:
        for k, v in contacts.items():
            print(k, v)


def unknown_command(user_input):
    print("Please repeat command")


contacts = {}

commands = {

    "add": func_add,
    "change": func_change,
    "phone": func_phone,
    "show": func_show_all
}


def main():

    global contacts, user_input

    print("Hallo, I am Bot! My commands:\n"
          "add new contact - add name phone\n"
          "change current contact - change name phone\n"
          "show phone - phone name\n"
          "show all contacts - show all")

    while True:
        user_input = input("Enter your command: ").lower()

        if user_input in (".", "good bye", "close", "exit"):
            print("Good bye!")
            break
        # вибираємо із словника commands необхідну функцію відповідно до команди яка була введена користувачем
        handler = commands.get(user_input.split()[0], unknown_command)
        handler(user_input)


main()
