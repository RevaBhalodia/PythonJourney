def second_highest_frequency(s):
    freq = {}

    # Count frequency
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

  
    unique_freq = list(set(freq.values()))

    if len(unique_freq) < 2:
        return None

    unique_freq.sort(reverse=True)

    second_highest = unique_freq[1]

   
    for ch in freq:
        if freq[ch] == second_highest:
            return ch


string = input("Enter a string: ")
result = second_highest_frequency(string)

if result:
    print("Character with second highest frequency:", result)
else:
    print("No second highest frequency found")