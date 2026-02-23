def sort_students_by_marks(data):

    sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)

    result = [name for name, marks in sorted_items]

    return result

students = {"A": 80, "B": 95, "C": 70}
print(sort_students_by_marks(students))