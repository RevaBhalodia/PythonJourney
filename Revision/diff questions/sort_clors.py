def sort_colors(nums):
    l, i, r = 0, 0, len(nums)-1

    while i <= r:
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        else:
            i += 1

# Example
arr = [2,0,2,1,1,0] 
sort_colors(arr)
print(arr)  # Output: [0,0,1,1,2,2]
