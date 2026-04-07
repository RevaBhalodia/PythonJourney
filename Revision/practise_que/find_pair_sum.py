def find_pair(arr, target):
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            return (num, complement)
        seen.add(num)

    return None

numbers = [2, 7, 11, 15]
print(find_pair(numbers, 9))