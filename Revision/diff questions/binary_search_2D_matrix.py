def search_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])

    l, r = 0, rows * cols - 1

    while l <= r:
        mid = (l+r)//2

        row = mid // cols
        col = mid % cols

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            l = mid + 1
        else:
            r = mid - 1

    return False
# Example
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
print(search_matrix(matrix, 3))  # Output: True
print(search_matrix(matrix, 13)) # Output: False
