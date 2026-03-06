lst = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(lst)
result = []

for i in lst:
    count = lst.count(i)
    if count > n/3 and i not in result:
        result.append(i)

print("Elements:", result)