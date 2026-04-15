responses = {
    "hi": "Hello!",
    "how are you": "I'm fine 😊",
    "bye": "Goodbye!"
}

while True:
    msg = input("You: ").lower()

    if msg in responses:
        print("Bot:", responses[msg])
    else:
        print("Bot: I don't understand")

    if msg == "bye":
        break