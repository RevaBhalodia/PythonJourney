parking = ["Empty"] * 10

while True:

    print("\n1. Park Car")
    print("2. Remove Car")
    print("3. Show Parking")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        car = input("Enter car number: ")

        if "Empty" in parking:
            index = parking.index("Empty")
            parking[index] = car
            print("Car parked at space", index + 1)
        else:
            print("Parking Full")

    elif choice == 2:
        car = input("Enter car number to remove: ")

        if car in parking:
            index = parking.index(car)
            parking[index] = "Empty"
            print("Car removed")
        else:
            print("Car not found")

    elif choice == 3:
        print("\nParking Status:")
        for i in range(len(parking)):
            print("Space", i+1, ":", parking[i])

    elif choice == 4:
        break