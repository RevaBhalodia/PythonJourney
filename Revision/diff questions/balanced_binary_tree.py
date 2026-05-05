def is_balanced(root):
    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return dfs(root) != -1
# Example usage:
# Given a binary tree, determine if it is height-balanced.
# For example, given the following binary tree,
#       1   
#      / \
#     2   3
#    / \
#   4   5
# Return true, as the tree is balanced.
# Given the following binary tree,
#       1
#      /
#     2
#    /
#   3
# Return false, as the tree is not balanced.
