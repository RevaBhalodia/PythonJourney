#1
def prime_dict(lst):
    result = {}
    
    for num in lst:
        if num < 2:
            result[num] = "not prime"
        else:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                result[num] = "prime"
            else:
                result[num] = "not prime"
    
    return result
print(prime_dict([1, 2, 3, 4, 5]))


#2
def lowest_score(d):
    lowest = min(d.values())
    
    for name in d:
        if d[name] == lowest:
            print("Lowest score is by:", name)
            break
scores = {"Aman": 85, "Riya": 72, "Karan": 90}
lowest_score(scores)


#3
def remainder_dict(lst):
    result = {}
    
    for num in lst:
        r = num % 3
        
        if r not in result:
            result[r] = []
        
        result[r].append(num)
    
    return result
print(remainder_dict([1, 2, 3, 4, 5, 6, 7]))
