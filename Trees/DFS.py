class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class DepthFirstSearch:

    def dfs(self, root):
        """
        Performs DFS starting from the root node.
        Parameters
        ----------
        root : TreeNode
            The root node of the binary tree.
        Returns
        -------
        None
        Notes
        -----
        - This method uses an iterative approach with a stack.
        - Modify the section marked with "Process the current node" to perform specific tasks (e.g., collecting values, checking conditions).
        - Modify the section marked with "Push the right/left child" to change the traversal order or add additional conditions.
        """
        stack = []
        # If the root is None, return
        if not root:
            return
        
        # Initialize the stack with the root node
        stack.append(root)
        
        # While there are nodes to process in the stack
        while stack:
            # Pop a node from the stack
            node = stack.pop()
            
            # Process the current node (e.g., print its value)
            print(node.val)
            
            # Push the left child to the stack if it exists
            if node.left:
                stack.append(node.left)
                
            # Push the right child to the stack if it exists
            if node.right:
                stack.append(node.right)
            
            