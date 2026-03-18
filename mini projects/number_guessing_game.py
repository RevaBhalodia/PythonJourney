# AI Number Guessing Game

low = 1
high = 100

print("Think of a number between 1 and 100")

while True:
    guess = (low + high) // 2
    print("AI guesses:", guess)

    feedback = input("Enter (h) too high, (l) too low, (c) correct: ")

    if feedback == 'c':
        print("AI guessed correctly!")
        break
    elif feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1