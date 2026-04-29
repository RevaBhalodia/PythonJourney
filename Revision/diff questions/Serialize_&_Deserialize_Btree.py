class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def serialize(root):
    res = []

    def dfs(node):
        if not node:
            res.append("N")
            return
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(res)

def deserialize(data):
    vals = data.split(",")
    i = 0

    def dfs():
        nonlocal i
        if vals[i] == "N":
            i += 1
            return None
        node = TreeNode(int(vals[i]))
        i += 1
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()
# Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
serialized = serialize(root)
print(serialized)  # "1,2,N,N,3,4,N,N,5,N,N"
deserialized = deserialize(serialized)
print(deserialized.val)  # 1
print(deserialized.left.val)  # 2
print(deserialized.right.val)  # 3
print(deserialized.right.left.val)  # 4
print(deserialized.right.right.val)  # 5
