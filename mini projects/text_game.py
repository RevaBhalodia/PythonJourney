# Adventure Game

print("Welcome to the Adventure Game!")
choice1 = input("You are in a forest. Go left or right? ")

if choice1.lower() == "left":
    choice2 = input("You see a river. Swim or walk? ")
    
    if choice2.lower() == "swim":
        print("You were eaten by a crocodile 🐊 Game Over")
    else:
        print("You found a village 🎉 You Win!")

elif choice1.lower() == "right":
    choice2 = input("You see a cave. Enter or run? ")
    
    if choice2.lower() == "enter":
        print("A lion attacked you 🦁 Game Over")
    else:
        print("You escaped safely 🎉 You Win!")

else:
    print("Invalid choice. Game Over")