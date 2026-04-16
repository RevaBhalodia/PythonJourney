import random

while True:
    input("Press Enter to roll dice")
    print("You got:", random.randint(1, 6))

    ch = input("Roll again? (y/n): ")
    if ch != 'y':
        break