'''Binary search tree -- Is a binary tree in which at each node, left child will have data less than or equal to its data
and right child will have data greater than its data.'''

from Binary_tree import * #Refer Binary Tree in Data Structures
 
class Binary_search_tree(Binary_tree):
    def __init__(self,root_key):
        super().__init__(root_key)

    #Time Complexity -- O(n) -- For unbalanced binray search tree
    def add_key(self,key,root):
        if not root:
            return Node(key)
        elif key<=root.data:
            root.left=self.add_key(key,root.left)
        else:
            root.right=self.add_key(key,root.right)
        return root
        
    #Time Complexity -- O(n) -- For unbalanced binray search tree
    def delete_node(self, node, root):
        if not root:
            return None

        # Traverse to find the node and its parent
        parent = None
        current = root
        while current and current != node:
            parent = current
            if node.data <= current.data:
                current = current.left
            else:
                current = current.right

        # If node was not found, return the unchanged root
        if not current:
            return root

        # Handle deletion (current == node)
        # Case 1: Node is a leaf
        if self.is_leaf(node):
            if parent is None:  # Node is the root
                root = None
            elif parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return root

        # Case 2: Node has one child
        if not node.left:
            if parent is None:  # Node is the root
                root = node.right
            elif parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
            return root
        if not node.right:
            if parent is None:  # Node is the root
                root = node.left
            elif parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
            return root

        # Case 3: Node has two children
        # Find the in-order successor (smallest node in right subtree)
        successor = node.right
        successor_parent = node
        while successor.left:
            successor_parent = successor
            successor = successor.left

        # Replace node's data with successor's data
        node.data = successor.data

        # Delete the successor (it has at most one right child)
        if successor_parent == node:
            successor_parent.right = successor.right
        else:
            successor_parent.left = successor.right

        return root
