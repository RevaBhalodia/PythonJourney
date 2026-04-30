def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero = False

    for r in range(rows):
        if matrix[r][0] == 0:
            row_zero = True
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[0][c] = matrix[r][0] = 0

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for c in range(cols):
            matrix[0][c] = 0

    if row_zero:
        for r in range(rows):
            matrix[r][0] = 0
# Example
mat = [
[1,1,1],
[1,0,1],        
[1,1,1]
]
set_zeroes(mat)
print(mat)
# Output: [[1,0,1],[0,0,0],[1,0,1]] 
