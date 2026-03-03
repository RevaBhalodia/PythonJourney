def analyze_scores(data):
    # -------- Highest Total Marks --------
    highest_student = ""
    highest_total = 0

    for student in data:
        total = 0
        for subject in data[student]:
            total += data[student][subject]

        if total > highest_total:
            highest_total = total
            highest_student = student

    # -------- Subject Highest Average --------
    subject_totals = {}
    student_count = len(data)

    for student in data:
        for subject in data[student]:
            if subject not in subject_totals:
                subject_totals[subject] = 0
            subject_totals[subject] += data[student][subject]

    highest_subject = ""
    highest_average = 0

    for subject in subject_totals:
        avg = subject_totals[subject] / student_count
        if avg > highest_average:
            highest_average = avg
            highest_subject = subject

    return highest_student, highest_total, highest_subject, highest_average


# Main Data
data = {
    "A": {"math": 80, "science": 90},
    "B": {"math": 70, "science": 60}
}

student, total, subject, average = analyze_scores(data)

print("Student with highest total:", student, "→", total)
print("Subject with highest average:", subject, "→", average)