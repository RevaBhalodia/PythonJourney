def remove_digits(s):
    result = ""

    for ch in s:
        if not ch.isdigit():
            result += ch

    return result


# Example
text = input("Enter a string: ")
print(remove_digits(text))