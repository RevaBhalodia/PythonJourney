#Write a function that takes a list of marks and returns:average marks,highest marks,
def marks_analysis(marks):
    average = sum(marks) / len(marks)
    highest = max(marks)
    return average, highest

marks = [78, 85, 90, 66, 88]
avg, high = marks_analysis(marks)

print("Average Marks:", avg)
print("Highest Marks:", high)

#Write a function that takes a sentence and returns the count of vowels
def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0

    for char in sentence:
        if char in vowels:
            count += 1

    return count

text = "Plenty of people are good-looking. That does not make them interesting or intriguing or cool."
print("Number of vowels:", count_vowels(text))
