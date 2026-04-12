users = {
    "admin": "1234",
    "rico": "pass123"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful")
else:
    print("Invalid credentials")