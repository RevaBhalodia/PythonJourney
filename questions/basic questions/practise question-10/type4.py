def is_valid_palindrome(s):
    cleaned = ""

    for ch in s:
        if ch.isalnum():  
            cleaned += ch.lower()

   
    return cleaned == cleaned[::-1]

print(is_valid_palindrome("A man, a plan, a canal: Panama"))
