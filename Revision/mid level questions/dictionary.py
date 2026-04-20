# Student score tracker
scores = {"Alice": 88, "Bob": 72, "Carol": 95}

# Safe access with default
print(scores.get("Dave", 0))   # 0 instead of KeyError

# Loop over key-value pairs
for name, score in scores.items():
    grade = "A" if score >= 90 else "B" if score >= 70 else "C"
    print(f"{name}: {score} → {grade}")

# Merge another dict
scores.update({"Dave": 80, "Eve": 91})

# Count character frequency
word = "mississippi"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)