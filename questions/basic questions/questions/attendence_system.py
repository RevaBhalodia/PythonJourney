
full_class = ["Amit", "Riya", "Raj", "Sneha", "Karan", "Priya"]

present_today = ["Amit", "Raj", "Sneha"]

absent_students = []
for student in full_class:
    if student not in present_today:
        absent_students.append(student)


total_students = len(full_class)
present_count = len(present_today)

attendance_percentage = (present_count / total_students) * 100


print("Total Students:", total_students)
print("Present Today:", present_count)
print("Attendance Percentage:", attendance_percentage, "%")

print("\nAbsent Students:", absent_students)


if attendance_percentage < 75:
    print("\n Attendance below 75%")
    print("Students present today:", present_today)
