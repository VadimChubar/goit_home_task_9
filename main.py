'''
user_input.split()[-1] ->  вибирааємо із строки що ввів коричтувач останній обєкт рахуємо що це має бути номер
' '.join(user_input.split()[0:-1]) -> вибираємо з початку строки все до останнього оюєкта
і обєднуємо знову в строку так як результат відбору список
'''


contacts =  {}

def input_error(func):
    def wrapper(user_input):
        # перевірка що номер який додається або змінюється складається тільки з цифр
        try:
            user_input.split()[-1] = int(user_input.split()[-1])
        except ValueError:
            print(f"Phone {user_input.split()[-1]} is not number, try again")

        result = func(user_input)
        return result
    return wrapper


@input_error
def func_add(user_input):
    global contacts
    user_input = user_input[3:].strip() # обрізаємо команду
    contacts[' '.join(user_input.split()[0:-1])] = user_input.split()[-1] #додаємо контакт у словник
    return  contacts

# треба перевірка що контакт номер якого треба замінити існує в словнику
# треба перевірка що словник не порожній
@input_error
def func_change(user_input):
    global contacts
    user_input = user_input[6:].strip()  # обрізаємо команду
    contacts.pop(' '.join(user_input.split()[0:-1])) # видаляємо контакт який треба змінити
    contacts[' '.join(user_input.split()[0:-1])] = user_input.split()[-1] #додаємо новий номер до існуючого контакту
    return contacts

def func_phone(user_input):
    global contacts
    return contacts.get(user_input[6:].strip(),"There is no such contact")

# треба перевірка що словник не порожній
def func_show_all(user_input):
    global contacts
    return contacts

def main():

    global contacts

    print("Hallo, I am Bot! My commands:\n"
          "add new contact - add name phone\n"
          "change current contact - change name phone\n"
          "show phone - phone name\n"
          "show all contacts - show all")
    while True:

        user_input = input("Enter your command: ")

        if user_input in (".", "good bye", "close", "exit"):
            print("Good bye!")
            break

        if user_input == 'hello':
            print("How can I help you?")

        if user_input[0:3].lower() == 'add':
            contacts = func_add(user_input)

        if user_input[0:6].lower() == 'change':
            contacts = func_change(user_input)

        if user_input[0:5].lower() == 'phone':
            print(func_phone(user_input))

        if user_input[0:8].lower() == 'show all':
            print(func_show_all(user_input))
#треба перевірити коректність команди

main()

