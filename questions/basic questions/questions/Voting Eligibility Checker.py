people = {
    "Rahul": 22,
    "Neha": 17,
    "Amit": 19,
    "Riya": 15
}

for name, age in people.items():

    if age >= 18:
        print(name, "is eligible to vote")

    else:
        print(name, "is not eligible to vote")