def plagiarism_score(text1, text2):
    set1 = set(text1.lower().split())
    set2 = set(text2.lower().split())

    intersection = len(set1 & set2)
    union = len(set1 | set2)

    return intersection / union

t1 = "Python is easy and powerful"
t2 = "Python is powerful and easy to learn"

print(plagiarism_score(t1, t2))