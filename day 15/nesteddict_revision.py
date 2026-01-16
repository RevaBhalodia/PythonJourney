#Create a nested dictionary for a student containing:
# Name,Roll number,Marks in Math and Science,Print the marks of Math.

student = {
    "name" : "mike wheeler",
    "roll number" : 107 ,
    "marks" :{
        "math" : 89,
        "science" : 90
        }
}
print(student)
print(student["marks"]["math"])


'''
Given:
students = {
    "student1": {"name": "Amit", "age": 21},
    "student2": {"name": "Riya", "age": 20}
}
Print the age of student2.
'''

students = {
    "student1": {"name": "Amit", "age": 21},
    "student2": {"name": "Riya", "age": 20}
}

print(students["student2"]["age"])