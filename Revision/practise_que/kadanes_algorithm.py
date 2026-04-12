def max_subarray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


arr = [-2, 3, 4, -1, 5, -6]
print("Maximum subarray sum:", max_subarray(arr))