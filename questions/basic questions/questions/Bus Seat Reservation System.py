seats = ["Available"] * 12

while True:

    print("\n1. View Seats")
    print("2. Book Seat")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:

        for i in range(len(seats)):
            print("Seat", i+1, ":", seats[i])

    elif choice == 2:

        seat = int(input("Enter seat number: "))

        if seats[seat-1] == "Available":
            seats[seat-1] = "Booked"
            print("Seat booked successfully")
        else:
            print("Seat already booked")

    elif choice == 3:
        break