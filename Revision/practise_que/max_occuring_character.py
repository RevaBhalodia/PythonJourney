def max_occurring_char(s):
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    max_char = max(freq, key=freq.get)
    return max_char


print(max_occurring_char("programming"))