class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, node, val):
        """
        Inserts a value into the binary search tree.
        
        Parameters:
            val (int): The value to be inserted.
        """
        if not self.root:
            self.root = TreeNode(val)
        else:
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    self.insert(node.left, val)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    self.insert(node.right, val)

    def remove(self, node, val):
        """
        Removes a value from the binary search tree.
        
        Parameters:
            val (int): The value to be removed.
        """
        if not node:
            return node
        if val < node.val:
            node.left = self.remove(node.left, val)
        elif val > node.val:
            node.right = self.remove(node.right, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self.remove(node.right, temp.val)
        return node
    
    def search(self, node, val):
        """
        Searches for a value in the binary search tree.
        
        Parameters:
            val (int): The value to be searched.
        """
        if not node or node.val == val:
            return node
        if val < node.val:
            return self.search(node.left, val)
        return self.search(node.right, val)
    
    def _min_value_node(self, node):
        """
        Find the node with the minimum value in a given binary search tree (BST) subtree.

        Args:
            node (TreeNode): The root node of the subtree.

        Returns:
            TreeNode: The node with the minimum value in the subtree.
        """
        current = node
        while current.left:
            current = current.left
        return current
    
    def _max_value_node(self, node):
        """
        Find the node with the maximum value in a given binary search tree (BST) subtree.

        Args:
            node (TreeNode): The root node of the subtree.

        Returns:
            TreeNode: The node with the maximum value in the subtree.
        """
        current = node
        while current.right:
            current = current.right
        return current

if __name__ == '__main__':
    bst = BinarySearchTree()
    
    # Insert nodes into the BST
    bst.insert(bst.root, 10)  # Root node
    bst.insert(bst.root, 5)   # Left child of root
    bst.insert(bst.root, 15)  # Right child of root
    bst.insert(bst.root, 3)   # Left child of node with value 5
    bst.insert(bst.root, 7)   # Right child of node with value 5
    bst.insert(bst.root, 12)  # Left child of node with value 15
    bst.insert(bst.root, 18)  # Right child of node with value 15
    
    # Visualization of the BST:
    #         10
    #        /  \
    #       5    15
    #      / \   / \
    #     3   7 12  18
    
    # Search for a node in the BST
    result = bst.search(bst.root, 7)
    print(result.val if result else "Not found")  # Expected output: 7
    
    # Remove a node from the BST
    bst.remove(bst.root, 10)
    
    # Visualization of the BST after removing 10:
    #         12
    #        /  \
    #       5    15
    #      / \     \
    #     3   7    18
    
    # Search for the removed node
    result = bst.search(bst.root, 10)
    print(result.val if result else "Not found")  # Expected output: Not found

    print(bst._min_value_node(bst.root).val)  # Expected output: 3
    print(bst._max_value_node(bst.root).val)  # Expected output: 18