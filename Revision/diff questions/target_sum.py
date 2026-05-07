def find_target_sum_ways(nums, target):
    dp = {0: 1}

    for num in nums:
        next_dp = {}

        for total, count in dp.items():
            next_dp[total + num] = next_dp.get(total + num, 0) + count
            next_dp[total - num] = next_dp.get(total - num, 0) + count

        dp = next_dp

    return dp.get(target, 0)
# Example usage:
# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
# Find out how many ways to assign symbols to make the sum of integers equal to target S.
# For example, given the list of integers [1, 1, 1, 1, 1] and target S = 3, there are 5 ways to assign symbols to make the sum of integers equal to target 3.
# -1+1+1+1+1 = 3    
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# Therefore, the output is 5.