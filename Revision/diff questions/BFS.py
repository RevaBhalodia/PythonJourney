from collections import deque

def level_order(root):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(level)

    return res
# Example usage:
# Given a binary tree, return the level order traversal of its nodes' values.   
# For example, given a binary tree, return the level order traversal of its nodes' values.
