def flatten(root):
    if not root:
        return

    flatten(root.left)
    flatten(root.right)

    left = root.left
    right = root.right

    root.left = None
    root.right = left

    curr = root
    while curr.right:
        curr = curr.right

    curr.right = right

# Example usage:
# Given a binary tree, flatten it to a linked list in-place.
# For example, given the following tree:
#     1 
#    / \
#   2   5   
#  / \   \
# 3   4   6
# The flattened tree should look like:  
# 1
#  \
#   2   
#    \
#     3
#      \
#       4   
#        \
#         5
#          \
#           6
