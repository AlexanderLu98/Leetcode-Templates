class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class PostOrder:
    """
    A class to perform post-order traversal on a binary tree.
    Post-order traversal visits nodes in the following order: left subtree, right subtree, root node.
    This traversal is suitable for tasks that require processing nodes after their subtrees have been processed,
    such as deleting a tree, evaluating expressions, or performing operations that need to consider child nodes before their parent nodes.
    """

    def __init__(self):
        self.stack = []

    def postorder_recursive(self, root):
        """
        Perform post-order traversal of a binary tree recursively.
        :param root: TreeNode, the root of the binary tree
        :return: List[int], the post-order traversal of the tree
        """
        if not root:
            return []
        return self.postorder_recursive(root.left) + self.postorder_recursive(root.right) + [root.val]
    
    def postorder_iterative(self, root):
        """
        Perform post-order traversal of a binary tree iteratively.
        :param root: TreeNode, the root of the binary tree
        :return: List[int], the post-order traversal of the tree
        """
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]
    
if __name__ == "__main__":
    p = PostOrder()
    # Example 1
    # Tree structure:
    #     1
    #      \
    #       2
    #      / \
    #     3   4
    #        /
    #       5
    # Expected output: [3, 5, 4, 2, 1]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    print(p.postorder_iterative(root))  # Output: [3, 5, 4, 2, 1]
    print(p.postorder_recursive(root))  # Output: [3, 5, 4, 2, 1]

    # Example 2
    # Tree structure:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    # Expected output: [4, 5, 2, 3, 1]
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    print(p.postorder_iterative(root2))  # Output: [4, 5, 2, 3, 1]
    print(p.postorder_recursive(root2))  # Output: [4, 5, 2, 3, 1]

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
    print(p.postorder_iterative(root3))  # Output: [3, 2, 1]
    print(p.postorder_recursive(root3))  # Output: [3, 2, 1]

    # Example 4
    # Tree structure:
    #     1
    #      \
    #       2
    #        \
    #         3
    # Expected output: [3, 2, 1]
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    print(p.postorder_iterative(root4))  # Output: [3, 2, 1]
    print(p.postorder_recursive(root4))  # Output: [3, 2, 1]