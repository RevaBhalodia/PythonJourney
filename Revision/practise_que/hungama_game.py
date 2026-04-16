import random

words = ["python", "developer", "engineer"]
word = random.choice(words)

guessed = ""
attempts = 6

while attempts > 0:
    display = ""

    for ch in word:
        if ch in guessed:
            display += ch
        else:
            display += "_"

    print(display)

    if display == word:
        print("You win!")
        break

    guess = input("Guess a letter: ")
    guessed += guess

    if guess not in word:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)