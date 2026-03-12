email = input("Enter email: ")

if email.count("@") != 1:
    print("Invalid Email")

else:
    username, domain = email.split("@")

    if username == "" or domain == "":
        print("Invalid Email")

    else:
        if "." in domain:
            print("Valid Email")
        else:
            print("Invalid Email")