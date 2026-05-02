def max_area(height):
    l, r = 0, len(height) - 1
    max_water = 0

    while l < r:
        h = min(height[l], height[r])
        width = r - l
        max_water = max(max_water, h * width)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_water

# Example
print(max_area([1,8,6,2,5,4,8,3,7]))  # Output: 49