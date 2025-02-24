'''BInary search tree -- Is a binary tree in which at each node, left child will have data less than or equal to its data
and right child will have data greater than its data.'''

from Binary_tree import * #Refer Binary Tree in Data Structures
class Binary_search_tree(Binary_tree):
    def __init__(self,root_key):
        super().__init__(root_key)

    #Time Complexity -- O(n) -- For unbalanced binray search tree
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
        
    #Time Complexity -- O(n) -- For unbalanced binray search tree
    def delete_node(self,node,root):
        if self.is_leaf(node):
            temp=root
            if temp==node:
                self.root=None
                return
            prev=temp
            while temp!=node:
                prev=temp
                if node.data<=temp.data:
                    temp=temp.left
                else:
                    temp=temp.right
                prev.data=temp.data
            if prev.left==node:
                prev.left=None
            else:
                prev.right=None
            
        elif node.right and node.left:
            temp=node.right
            prev=node
            while temp.left:
                prev=temp
                temp=temp.left
            if self.is_leaf(temp):
                node.data=temp.data
                if prev==node:
                    node.right=None
                else:
                    prev.left=None
            else:
                node.data=temp.data
                if prev==node:
                    node.right=temp.right
                else:
                    prev.left=temp.right
                
        else:
            if not node.right:
                node.data=node.left.data
                node.left=None
            else:
                node.data=node.right.data
                node.right=None
                
                
