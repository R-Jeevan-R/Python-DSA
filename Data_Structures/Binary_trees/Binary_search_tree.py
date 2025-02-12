'''Binary search tree -- Is a binary tree in which at each node, left child will have data less than or equal to its data
and right child will have data greater than its data.'''

from Binary_tree import *
class Binary_search_tree(Binary_tree):
    def __init__(self,root_key):
        super().__init__(root_key)

    #Time Complexity -- O(n) -- For unbalanced binray tree
    def add_key(self,key,root):
        if not root:
            root=Node(key)
            return root
        elif key<=root.data:
            root.left=self.add_key(key,root.left)
            return root
        else:
            root.right=self.add_key(key,root.right)
            return root

    def delete_key(self,key,root):
        pass

    
        
    

