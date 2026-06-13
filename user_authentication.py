import os
import json

flag = True


def login():
    print("This is login page\n")

    user_name = input("Username: ")
    password = input("Password: ")

    verify(uname=user_name, pw=password)


def register():
    user_name = input("Enter your new username: ")
    password = input("Enter your new password: ")

    user = {
        'username': user_name,
        'password': password
    }

    save_info(user)


def save_info(u_info):
    with open('user_info.json', mode='w',encoding="utf-8") as file_writer:
        json.dump(u_info, file_writer, indent=2)

    print("Your registration is completed.\n")


def verify(uname, pw):
    global flag

    try:
        with open('user_info.json', mode='r',encoding="utf-8") as file_reader:
            user = json.load(file_reader)

        if user['username'] == uname and user['password'] == pw:
            flag = False  # Stops the root while loop
            main_menu()

        else:
            print("Incorrect username or password, please try again!\n")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please register first.\n")


def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Access Granted!")


while flag:
    option = input(
        "Welcome to Crazon X Bank\n"
        "1. Login\n"
        "2. Register\n"
        "Type 'exit' to quit\n"
        "Your option: "
    )

    if option == '1':
        login()

    elif option == '2':
        register()

    elif option.lower() == 'exit':
        print("Bye bye.")
        flag = False

    else:
        print("Invalid option, please try again.\n")

print("Program continues here after the loop ends.")