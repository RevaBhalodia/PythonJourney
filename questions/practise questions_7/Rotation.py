def rotate_right(nums, k):
    n = len(nums)
    
    # Handle k greater than length
    k = k % n
    
    return nums[-k:] + nums[:-k]


# Main Program
nums = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter value of k: "))

result = rotate_right(nums, k)
print("Rotated List:", result)