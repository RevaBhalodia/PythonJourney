def group_by_first_letter(words):
    result = {}

    for word in words:
        first_char = word[0]

        if first_char in result:
            result[first_char].append(word)
        else:
            result[first_char] = [word]

    return result


# Example
print(group_by_first_letter(["apple", "ant", "bat", "ball"]))