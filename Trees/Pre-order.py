class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class PreOrder():
    """
    Pre-order traversal is a depth-first traversal method where the nodes are recursively visited in this order:
    1. Visit the root node.
    2. Traverse the left subtree.
    3. Traverse the right subtree.
    This traversal method is used when you need to explore the root node before inspecting any of its children. It is useful in scenarios where you want to create a copy of the tree, prefix notation of an expression tree, or when you need to evaluate the nodes in a hierarchical manner.
    """

    def __init__(self):
        """
        Initializes the PreOrder class with an empty stack.
        """
        self.stack = []

    def preorder_recursive(self, root):
        """
        Performs pre-order traversal of the binary tree recursively.
        
        Parameters:
            root (TreeNode): The root node of the binary tree.
        
        Returns:
            List[int]: A list of node values in pre-order.
        """
        if not root:
            return []
        return [root.val] + self.preorder_recursive(root.left) + self.preorder_recursive(root.right)

    def preorder_iterative(self, root):
        """
        Performs pre-order traversal of the binary tree iteratively.
        
        Parameters:
            root (TreeNode): The root node of the binary tree.
        
        Returns:
            List[int]: A list of node values in pre-order.
        """
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result
    
if __name__ == "__main__":
    p = PreOrder()

    # Example 1
    # Tree structure:
    #     1
    #      \
    #       2
    #      / \
    #     3   4
    #        /
    #       5
    # Expected output: [1, 2, 3, 4, 5]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    print(p.preorder_iterative(root))  # Output: [1, 2, 3, 4, 5]
    print(p.preorder_recursive(root))  # Output: [1, 2, 3, 4, 5]

    # Example 2
    # Tree structure:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    # Expected output: [1, 2, 4, 5, 3]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    print(p.preorder_iterative(root2))  # Output: [1, 2, 4, 5, 3]
    print(p.preorder_recursive(root2))  # Output: [1, 2, 4, 5, 3]

    # Example 3
    # Tree structure:
    #     1
    #    /
    #   2
    #  /
    # 3
    # Expected output: [1, 2, 3]
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    print(p.preorder_iterative(root3))  # Output: [1, 2, 3]
    print(p.preorder_recursive(root3))  # Output: [1, 2, 3]

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
    print(p.preorder_iterative(root4))  # Output: [1, 2, 3]
    print(p.preorder_recursive(root4))  # Output: [1, 2, 3]