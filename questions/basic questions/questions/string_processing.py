sentence = input("Enter a sentence: ")

characters = len(sentence)
words = len(sentence.split())

vowels = "aeiouAEIOU"
vowel_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1

print("Characters:", characters)
print("Words:", words)
print("Vowels:", vowel_count)