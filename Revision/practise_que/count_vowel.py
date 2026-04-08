def count_vowels(sentence):
    vowels = "aeiou"
    words = sentence.split()
    
    result = {}
    
    for word in words:
        count = 0
        for char in word.lower():
            if char in vowels:
                count += 1
        result[word] = count
    
    return result


print(count_vowels("Python is very powerful"))