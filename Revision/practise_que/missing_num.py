def find_missing(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)


arr = [1, 2, 3, 5, 6]
n = 6

print("Missing number:", find_missing(arr, n))