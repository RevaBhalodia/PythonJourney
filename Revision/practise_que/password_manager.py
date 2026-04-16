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
    site = input("Site: ")
    pwd = input("Password: ")
    data = load_data()
    data[site] = pwd
    save_data(data)
    print("Saved")

def get_password():
    site = input("Site: ")
    data = load_data()
    print("Password:", data.get(site, "Not found"))

while True:
    ch = input("1.Add 2.Get 3.Exit: ")
    if ch == "1":
        add_password()
    elif ch == "2":
        get_password()
    else:
        break