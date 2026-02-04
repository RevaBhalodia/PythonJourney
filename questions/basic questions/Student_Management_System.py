'''
Create a system to manage student data.
Use a class Student,
Attributes: name, roll_no, marks (list of 5 subjects)
Methods:
calculate total,calculate percentage,determine grade,Store multiple students in a list,
Save student details to a file,Read and display data from the file.
'''
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks   

    def calculate_total(self):
        return sum(self.marks)   

    def calculate_percentage(self):
        total = self.calculate_total()
        return total / 5

    def determine_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 75:
            return "A"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        else:
            return "Fail"


students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details for student", i + 1)
    name = input("Name: ")
    roll_no = input("Roll No: ")

    marks = []
    for j in range(5):
        m = int(input(f"Enter marks of subject {j + 1}: "))
        marks.append(m)

    student = Student(name, roll_no, marks)
    students.append(student)

with open("student_data.txt", "w") as file:
    for s in students:
        file.write(f"Name: {s.name}\n")
        file.write(f"Roll No: {s.roll_no}\n")
        file.write(f"Marks: {s.marks}\n")
        file.write(f"Total: {s.calculate_total()}\n")
        file.write(f"Percentage: {s.calculate_percentage()}\n")
        file.write(f"Grade: {s.determine_grade()}\n")
        file.write("-------------------------\n")

print("\nStudent details saved to file.")

print("\n--- Student Records from File ---")
with open("student_data.txt", "r") as file:
    data = file.read()
    print(data)
