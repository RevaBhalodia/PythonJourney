# question 1
def word_length_dict(sentence):
    words = sentence.split()
    return {word: len(word) for word in words}
print(word_length_dict("python is very easy"))


# question 2
def remove_failed_students(students):
    return {name: marks for name, marks in students.items() if marks >= 40}
students = {"mike": 75, "finn": 32, "nico": 40, "rico": 28}
print(remove_failed_students(students))


# question 3
def sort_dict_by_values(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))
marks = {"max": 75, "lucus": 85, "dustin": 60}
print(sort_dict_by_values(marks))
