import json

FILE = "passwords.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def add_password():
    site = input("Enter site: ")
    pwd = input("Enter password: ")

    data = load_data()
    data[site] = pwd
    save_data(data)

    print("Saved successfully")

def get_password():
    site = input("Enter site: ")
    data = load_data()

    if site in data:
        print("Password:", data[site])
    else:
        print("Not found")

while True:
    print("\n1.Add 2.Get 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_password()
    elif ch == "2":
        get_password()
    else:
        break
    