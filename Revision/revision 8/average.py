def closest_to_average(marks):
    avg = sum(marks.values()) / len(marks)
    
    closest_student = None
    min_diff = float('inf')
    
    for name, score in marks.items():
        diff = abs(score - avg)
        
        if diff < min_diff:
            min_diff = diff
            closest_student = name
    
    return closest_student

students = {
    "Alex": 80,
    "luke": 75,
    "haley": 90,
    "lily": 85
}

print(closest_to_average(students))
