class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ZigZagOrder:
    """
    Zigzag level-order traversal means traversing the tree level by level, but alternating the direction
    of traversal at each level. For example, the first level is traversed from left to right, the second
    level from right to left, the third level from left to right, and so on. This type of traversal is
    suitable for tasks where you need to process nodes in a specific zigzag pattern, such as in certain
    tree-based algorithms or when visualizing the tree structure in a zigzag manner.
    """
    def zigzag_order(self, root):
        """
        Traverse a binary tree in zigzag level order.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            List[List[int]]: A list of lists, where each inner list contains the values of the tree nodes at each level,
                             traversed in zigzag order (left to right, then right to left for the next level, and so on).
        """
        if not root:
            return []
        result = []
        queue = [root]
        zigzag = False
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if zigzag:
                result.append(level[::-1])
            else:
                result.append(level)
            zigzag = not zigzag
        return result
    
if __name__ == "__main__":
    # Example 1:
    # Tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    # Expected Output: [[1], [3, 2], [4, 5]]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    p = ZigZagOrder()
    print(p.zigzag_order(root1))  # Output: [[1], [3, 2], [4, 5]]

    # Example 2:
    # Tree:
    #     1
    #    / \
    #   2   3
    #  /     \
    # 4       5
    # Expected Output: [[1], [3, 2], [4, 5]]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    print(p.zigzag_order(root2))  # Output: [[1], [3, 2], [4, 5]]

    # Example 3:
    # Tree:
    #     1
    #    / \
    #   2   3
    #  /     \
    # 4       5
    #  \     /
    #   6   7
    # Expected Output: [[1], [3, 2], [4, 5], [7, 6]]
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.left.right = TreeNode(6)
    root3.right.right = TreeNode(5)
    root3.right.right.left = TreeNode(7)
    print(p.zigzag_order(root3))  # Output: [[1], [3, 2], [4, 5], [7, 6]]