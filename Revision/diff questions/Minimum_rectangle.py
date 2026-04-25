def largest_histogram(heights):
    stack = []
    max_area = 0
    heights.append(0)

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    heights.pop()
    return max_area

def maximal_rectangle(matrix):
    if not matrix:
        return 0

    cols = len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for i in range(cols):
            heights[i] = heights[i] + 1 if row[i] == "1" else 0

        max_area = max(max_area, largest_histogram(heights))

    return max_area

# Example
matrix = [
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]
]

print(maximal_rectangle(matrix))  # Output: 6