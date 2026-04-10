def check_anagram(s1, s2):
    s1 = sorted(s1.lower())
    s2 = sorted(s2.lower())

    if s1 == s2:
        return "Anagram"
    else:
        return "Not Anagram"


a = input("Enter first string: ")
b = input("Enter second string: ")

print(check_anagram(a, b))