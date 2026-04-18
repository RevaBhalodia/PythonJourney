def spiral_matrix(matrix):
    result = []

    if not matrix:
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Top row
        for i in range(left, right + 1):
            result.append(matrix[top])
        top += 1

        # Right column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Bottom row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom])
            bottom -= 1

        if left <= right:
            # Left column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral_matrix(matrix))