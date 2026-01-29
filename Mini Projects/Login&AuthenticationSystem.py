# login and authentication system

FILE_NAME = "users.txt"

def load_users():
    users = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        pass  
    return users

def register_user(users):
    username = input("Enter new username: ")

    if username in users:
        print(" Username already exists!")
        return

    password = input("Enter password: ")
    users[username] = password

    with open(FILE_NAME, "a") as file:
        file.write(username + "," + password + "\n")

    print(" Registration successful!")


def login_user(users):
    username = input("Enter username: ")

    if username not in users:
        print(" Username not found!")
        return

    password = input("Enter password: ")

    if users[username] == password:
        print(" Login successful! Welcome,", username)
    else:
        print(" Incorrect password!")


def main():
    users = load_users()

    while True:
        print("\n--- Login System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register_user(users)
        elif choice == "2":
            login_user(users)
        elif choice == "3":
            print(" Goodbye")
            break
        else:
            print(" Invalid choice!")

main()
