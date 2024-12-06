class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LevelOrder:
    """
    A class to perform level-order traversal (breadth-first traversal) on a binary tree.
    Level-order traversal visits nodes level by level from left to right. It starts at the root node,
    then visits all nodes at the next level, and so on. This traversal is suitable for tasks that require
    processing nodes in a hierarchical manner, such as finding the shortest path in an unweighted tree,
    or performing operations that need to consider nodes at the same depth together.
    """
    def __init__(self):
        self.stack = []
    def levelorder(self, root):
        """
        Perform a level-order traversal (breadth-first traversal) on a binary tree.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            List[List[int]]: A list of lists, where each inner list contains the values
                             of the nodes at each level of the binary tree.
        """
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
    
if __name__ == "__main__":
    # Example 1: Simple binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    p1 = LevelOrder()
    print("Level order traversal of tree 1:", p1.levelorder(root1))
    # Expected output: [[1], [2, 3], [4, 5]]

    # Example 2: Single node tree
    #   1
    root2 = TreeNode(1)
    p2 = LevelOrder()
    print("Level order traversal of tree 2:", p2.levelorder(root2))
    # Expected output: [[1]]

    # Example 3: Empty tree
    root3 = None
    p3 = LevelOrder()
    print("Level order traversal of tree 3:", p3.levelorder(root3))
    # Expected output: []

    # Example 4: Larger binary tree
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    #   / \
    #  8   9
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    root4.right.left = TreeNode(6)
    root4.right.right = TreeNode(7)
    root4.left.left.left = TreeNode(8)
    root4.left.left.right = TreeNode(9)
    p4 = LevelOrder()
    print("Level order traversal of tree 4:", p4.levelorder(root4))
    # Expected output: [[1], [2, 3], [4, 5, 6, 7], [8, 9]]