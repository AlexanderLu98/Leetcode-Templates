class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class ReverseLevelOrder:
    """
    Reverse level-order traversal means traversing the tree level by level from bottom to top,
    and within each level, from left to right. This type of traversal is suitable for tasks
    where you need to process nodes from the deepest level first, such as in certain tree-based
    algorithms or when visualizing the tree structure from bottom to top.
    """

    def __init__(self):
        self.stack = []
    def reverse_levelorder(self, root):
        """
        Perform a reverse level-order traversal on a binary tree.

        Args:
            root (TreeNode): The root node of the binary tree.

        Returns:
            List[List[int]]: A list of lists, where each sublist contains the values of the nodes
                             at each level of the tree, starting from the bottom level to the top.
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
            result.insert(0, level)
        return result
    
if __name__ == "__main__":
    # Example 1:
    # Tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    # Expected Output: [[4, 5], [2, 3], [1]]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    p1 = ReverseLevelOrder()
    print(p1.reverse_levelorder(root1))  # Output: [[4, 5], [2, 3], [1]]

    # Example 2:
    # Tree:
    #     1
    #    / \
    #   2   3
    #  /     \
    # 4       5
    # Expected Output: [[4, 5], [2, 3], [1]]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    p2 = ReverseLevelOrder()
    print(p2.reverse_levelorder(root2))  # Output: [[4, 5], [2, 3], [1]]

    # Example 3:
    # Tree:
    #     1
    #    / 
    #   2   
    #  /     
    # 3       
    # Expected Output: [[3], [2], [1]]
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    p3 = ReverseLevelOrder()
    print(p3.reverse_levelorder(root3))  # Output: [[3], [2], [1]]

    # Example 4:
    # Tree:
    #     1
    # Expected Output: [[1]]
    root4 = TreeNode(1)
    p4 = ReverseLevelOrder()
    print(p4.reverse_levelorder(root4))  # Output: [[1]]