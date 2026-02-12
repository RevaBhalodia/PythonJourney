def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    return s2 in (s1 + s1)



print(is_rotation("abcd", "cdab"))  
print(is_rotation("abcd", "acbd"))  
