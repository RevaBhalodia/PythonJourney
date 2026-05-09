from collections import deque

def right_side_view(root):
    if not root:
        return []

    res = []
    queue = deque([root])

    while queue:
        right_side = None

        for _ in range(len(queue)):
            node = queue.popleft()
            right_side = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(right_side.val)

    return res