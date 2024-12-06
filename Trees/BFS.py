from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
            
class BreadthFirstSearch:

    def bfs(self, root):
        """
        Performs BFS starting from the root node.
        Parameters
        ----------
        root : TreeNode
            The root node of the binary tree.
        Returns
        -------
        None
        Notes
        -----
        - This method uses an iterative approach with a queue.
        - Modify the section marked with "Process the current node" to perform specific tasks (e.g., collecting values, checking conditions).
        - Modify the section marked with "Enqueue the left/right child" to change the traversal order or add additional conditions.
        """
        queue = deque()
        # If the root is None, return
        if not root:
            return
        
        # Initialize the queue with the root node
        queue.append(root)
        
        # While there are nodes to process in the queue
        while queue:
            # Dequeue a node from the front of the queue
            node = queue.popleft()
            
            # Process the current node (e.g., print its value)
            print(node.val)
            
            # Enqueue the left child to the queue if it exists
            if node.left:
                queue.append(node.left)
                
            # Enqueue the right child to the queue if it exists
            if node.right:
                queue.append(node.right)