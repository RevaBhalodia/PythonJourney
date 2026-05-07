class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = self.random = None

def clone_tree(root):
    old_to_new = {}

    def dfs(node):
        if not node:
            return None

        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        old_to_new[node] = copy

        copy.left = dfs(node.left)
        copy.right = dfs(node.right)
        copy.random = dfs(node.random)

        return copy

    return dfs(root)
# Example usage:
# Given a binary tree, return a deep copy of the tree. Each node in the tree contains an additional random pointer which could point to any node in the tree or null.   
# For example, given the following binary tree,
#       1
#      / \
#     2   3
#    / \
#   4   5   
# Return a deep copy of the tree. The random pointer of each node in the new tree should point to the corresponding node in the new tree that the random pointer of the original node points to.
