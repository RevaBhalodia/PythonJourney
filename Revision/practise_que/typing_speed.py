import time

sentence = "python is powerful and easy to learn"

input("Press Enter to start...")

start = time.time()
typed = input("Type: ")
end = time.time()

time_taken = end - start
speed = len(typed.split()) / (time_taken / 60)

print("Time:", round(time_taken, 2), "seconds")
print("Speed:", round(speed, 2), "WPM")