#Student Result System (Using Functions)
'''
Calculate total marks, percentage, and result using functions.
Create functions for:
get_total(marks_list)
get_percentage(total)
get_result(percentage) → Pass / Fail
get_grade(percentage)
Pass if percentage ≥ 40 # rules
Grade:
≥ 75 → A
≥ 60 → B
≥ 40 → C
Else → Fail
Input
Marks of 5 subjects
'''

def get_total(marks_list):
    return sum(marks_list)

def get_percentage(total):
    return total / 5

def get_result(percentage):
    if percentage >= 40:
        return "pass"
    else:
        return "fail"

def get_grade(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "fail"
    
marks = []

print("enter marks of 5 subjects: ")
for i in range(5):
    mark = int(input(f"subject {i+1}: "))
    marks.append(mark)

total = get_total(marks)
percentage = get_percentage(total)
result = get_result(percentage)
grade = get_grade(percentage)

print("\n student result...")
print("total marks", total)
print("percentage:", percentage)
print("result:", result)
print("grade:", grade)