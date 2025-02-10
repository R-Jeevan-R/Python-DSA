'''Tree Traversal algorithms :
Inorder -- (Left,Root,Right) -- Traverses left child first followed by root and then right child at each node.
Preorder -- (Root,Left,Right) -- Traverses root first followed by left child and then right child at each node.
Postorder -- (Left,Right,Root) --- Traverses left child first followed by right child and root at last at each node.'''

##class Node():
##    def __init__(self,data):
##        self.left=None
##        self.data=data
##        self.right=None
##
##class Binary_tree():
##    def __init__(self,root_key):
##        self.root=Node(root_key)

class Traversals():
    def __init__(self):
        pass

    #Time Complexity -- O(n)
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=' ')
            self.inorder(root.right)
            
    #Time Complexity -- O(n)
    def preorder(self,root):
        if root:
            print(root.data,end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
            
    #Time Complexity -- O(n)
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=' ')

     
            
            
