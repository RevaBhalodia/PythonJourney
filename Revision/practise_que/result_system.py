students = {
    "Rico": [85, 78, 90],
    "Aman": [70, 88, 65],
    "Neha": [92, 80, 85]
}

for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)

    print("\nName:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", avg)

    if avg >= 75:
        print("Grade: A")
    elif avg >= 60:
        print("Grade: B")
    else:
        print("Grade: C")
        