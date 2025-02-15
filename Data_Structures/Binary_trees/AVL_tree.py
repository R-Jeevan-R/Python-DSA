'''AVL Tree -- Balanced Binary Search Tree.
Balance Factor, BF = Height(Right Sub Tree) - Height(Left Sub Tree).
In AVL tree the BF will be in {-1,0,1}.'''

from Binary_search_tree import *

class AVL_tree(Binary_search_tree):
    def __init__(self,root_key):
        super().__init__(root_key)

    #Every Insertion of key is followed by Balancing.
    #Time Complexity -- O(Logn)
    def insert_key(self,key,root):
        node = super().add_key(key,root)
        return self.balance(node)

    def get_balance(self,node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    #Time Complexity -- O(Logn)
    def balance(self,node):
        if not node:
            return
        balance=self.get_balance(node)
        
        # Left-Left (LL) Case → Right Rotation
        if balance>1 and self.get_balance(node.left)>=0:
            return self.rotate_right(node)
        
        # Right-Right (RR) Case → Left Rotation
        if balance <-1 and self.get_balance(node.right)<=0:
            return self.rotate_left(node)

        # Right-Left (RL) Case → Right rotation + Left Rotation
        if balance <-1 and self.get_balance(node.right)>0:
            node.right=self.rotate_right(node.right)
            return self.rotate_left(node)

        # Left-Right (LR) Case → Left Rotation + Right Rotation
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        return node #No rotation needed

    '''O(1) time for all rotations '''
    # Right Rotation (for LL case)
    def rotate_right(self,z):
        y=z.left
        t3=y.right

        y.right=z
        z.left=t3
        return y
    
    # Left Rotation (for RR case)
    def rotate_left(self,z):
        y=z.right
        t2=y.left

        y.left=z
        z.right=t2
        return y
        
