questions = {
    "Capital of India?": "delhi",
    "5 + 3 = ?": "8",
    "Python is language? (yes/no)": "yes",
    "everybody should love animals? (yes/no)": "yes"
}

score = 0

for q, ans in questions.items():
    user = input(q + " ").lower()

    if user == ans:
        score += 1

print("Final Score:", score, "/", len(questions))