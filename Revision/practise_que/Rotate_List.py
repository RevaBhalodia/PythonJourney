def rotate_right(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

numbers = [1, 2, 3, 4, 5]
print(rotate_right(numbers, 2))