def input_error(user_input):
    phone = user_input.split()[-1]

    try:
        phone = int(phone)
    except ValueError:
        print(f"Phone {phone} is not a number")
    finally:
        print(f"Add contact {user_input}")


a = input(':')
b = input_error(a)
print(b)

