correct_pin = 1234
attempts = 3

while attempts > 0:

    pin = int(input("Enter PIN: "))

    if pin == correct_pin:
        print("Access Granted")
        break

    else:
        attempts -= 1
        print("Wrong PIN")

if attempts == 0:
    print("Account Blocked")