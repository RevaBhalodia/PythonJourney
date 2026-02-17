def alternate_case(s):
    result = ""
    
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i].lower()
    
    return result


print(alternate_case("python"))
print(alternate_case("mike willer"))