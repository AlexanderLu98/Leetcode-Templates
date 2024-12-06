class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class InOrder():
    """
    In-order traversal is a depth-first traversal method where the nodes are recursively visited in the following order:
    1. Visit the left subtree
    2. Visit the root node
    3. Visit the right subtree
    This traversal method is suitable for tasks such as:
    - Retrieving the nodes of a binary search tree (BST) in ascending order.
    - Converting a binary tree into a sorted doubly linked list.
    - Generating a sorted array from a BST.
    """

    def __init__(self):
        """
        Initializes the in_order class with an empty stack.
        """
        self.stack = []

    def inorder_recursive(self, root):
        """
        Performs recursive in-order traversal on a binary tree.
        Args:
            root (TreeNode): The root node of the binary tree.
        Returns:
            List[int]: A list of node values in in-order sequence.
        """
        if not root:
            return []
        return self.inorder_recursive(root.left) + [root.val] + self.inorder_recursive(root.right)
    
    def inorder_iterative(self, root):
        """
        Performs iterative in-order traversal on a binary tree.
        Args:
            root (TreeNode): The root node of the binary tree.
        Returns:
            List[int]: A list of node values in in-order sequence.
        """
        if not root:
            return []
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
    
    def inorder_morris(self, root):
        """
        Performs Morris in-order traversal on a binary tree.
        Args:
            root (TreeNode): The root node of the binary tree.
        Returns:
            List[int]: A list of node values in in-order sequence.
        """
        res = []
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                if not pre.right:
                    pre.right = root
                    root = root.left
                else:
                    pre.right = None
                    res.append(root.val)
                    root = root.right
            else:
                res.append(root.val)
                root = root.right
        return res
   
if __name__ == "__main__":
    in_order = InOrder()

    # Example 1
    # Tree structure:
    #     1
    #      \
    #       2
    #      / \
    #     3   4
    #        /
    #       5
    # Expected output: [1, 3, 2, 5, 4]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    print(in_order.inorder_iterative(root))  # Output: [1, 3, 2, 5, 4]
    print(in_order.inorder_recursive(root))  # Output: [1, 3, 2, 5, 4]
    print(in_order.inorder_morris(root))     # Output: [1, 3, 2, 5, 4]

    # Example 2
    # Tree structure:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    # Expected output: [4, 2, 5, 1, 3]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    print(in_order.inorder_iterative(root2))  # Output: [4, 2, 5, 1, 3]
    print(in_order.inorder_recursive(root2))  # Output: [4, 2, 5, 1, 3]
    print(in_order.inorder_morris(root2))     # Output: [4, 2, 5, 1, 3]

    # Example 3
    # Tree structure:
    #     1
    #    /
    #   2
    #  /
    # 3
    # Expected output: [3, 2, 1]
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    print(in_order.inorder_iterative(root3))  # Output: [3, 2, 1]
    print(in_order.inorder_recursive(root3))  # Output: [3, 2, 1]
    print(in_order.inorder_morris(root3))     # Output: [3, 2, 1]

    # Example 4
    # Tree structure:
    #     1
    #      \
    #       2
    #        \
    #         3
    # Expected output: [1, 2, 3]
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    print(in_order.inorder_iterative(root4))  # Output: [1, 2, 3]
    print(in_order.inorder_recursive(root4))  # Output: [1, 2, 3]
    print(in_order.inorder_morris(root4))     # Output: [1, 2, 3]