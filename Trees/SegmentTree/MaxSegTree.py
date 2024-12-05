class MaxSegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        # Initialize leaves
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Build the tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, pos, value):
        # Update the value at the leaf node
        pos += self.n
        self.tree[pos] = value
        # Update the parents
        while pos > 1:
            pos //= 2
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, left, right):
        # Query the max in the range [left, right)
        result = float('-inf')
        left += self.n
        right += self.n
        while left < right:
            if left % 2:
                result = max(result, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                result = max(result, self.tree[right])
            left //= 2
            right //= 2
        return result

if __name__ == "__main__":
    s = MaxSegmentTree([1, 2, 3, 4, 5])
    print(s.query(1, 3))
    s.update(2, 10)
    print(s.query(1, 3))
    print(s.query(0, 5))