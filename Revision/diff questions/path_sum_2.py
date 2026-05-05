def path_sum(root, targetSum):
    res = []

    def dfs(node, path, total):
        if not node:
            return

        path.append(node.val)
        total += node.val

        if not node.left and not node.right and total == targetSum:
            res.append(path[:])

        dfs(node.left, path, total)
        dfs(node.right, path, total)

        path.pop()

    dfs(root, [], 0)
    return res
# Example usage:
# Given a binary tree and a target sum, return all root-to-leaf paths where each path's sum equals the target sum.
# For example, given the following binary tree and target sum = 22,
#       5
#      / \
#     4   8 
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
# [

#    [5,4,11,2],
#    [5,8,4,5]  
# ]
