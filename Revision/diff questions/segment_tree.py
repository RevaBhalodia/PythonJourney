class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, l, r):
        if l == r:
            self.tree[node] = nums[l]
            return
        mid = (l + r) // 2
        self.build(nums, 2*node+1, l, mid)
        self.build(nums, 2*node+2, mid+1, r)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        return self.query(2*node+1, l, mid, ql, qr) + \
               self.query(2*node+2, mid+1, r, ql, qr)

# Example
nums = [1,3,5,7,9,11]
st = SegmentTree(nums)
print(st.query(0,0,len(nums)-1,1,3))  # Output: 15