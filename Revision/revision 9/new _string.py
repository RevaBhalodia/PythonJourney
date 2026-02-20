def capitalize_words(s):
    words = s.split()
    result = ""

    for word in words:
        if len(word) > 0:
            first = word[0].upper()
            rest = word[1:].lower()
            result += first + rest + " "

    return result.strip()


text = input("Enter a string: ")
print(capitalize_words(text))