#Create a dictionary to store student names and marks.
#Print the name of the student who scored the highest marks.
students = {
    "eleven": 78,
    "nancy": 85,
    "max": 72,
    "mike": 90
}

highest_marks = 0
topper = ""

for name, marks in students.items():
    if marks > highest_marks:
        highest_marks = marks
        topper = name

print("Student with highest marks:", topper)


#Given a dictionary:prices = {"pen": 10, "book": 50, "bag": 400},Increase the price of each item by 10% and print the updated dictionary.
prices = {"pen": 10, "book": 50, "bag": 400}

for item in prices:
    prices[item] = prices[item] + (prices[item] * 10 / 100)

print(prices)
