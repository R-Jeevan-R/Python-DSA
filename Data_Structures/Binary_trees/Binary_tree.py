'''Binary tree -- A hierarchical data structure that stores data items in connected nodes.
Each node in binary tree will have maximum of two children i.e may have one or both left and right childs.
'''
import os
import sys

# Add the parent directory to sys.path to access sibling modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Algorithms.Traversal.Binary_tree_traversal_algo import Traversals

class Node():
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

class Binary_tree():
    def __init__(self,root_key = None):
        self.root = Node(root_key)

    #Time Complexity -- O(1)
    def is_leaf(self,node):
        if not node.left and not node.right:
            return True
        return False

    #TIme Complexity -- O(n)
    def height(self,root):
        if not root or self.is_leaf(root):
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    #TIme Complexity -- O(n)
    def number_of_nodes(self,root):
        if root:
            return 1 + self.number_of_nodes(root.left) + self.number_of_nodes(root.right)
        else:
            return 0

    #TIme Complexity -- O(n)
    def is_full(self,root):
        if self.is_leaf(root):
            return True
        elif root.right and root.left:
            return self.is_full(root.left) and self.is_full(root.right)
        else:
            return False
        
    #Time Complexity -- O(n)
    def number_of_leaves(self,root):
        if not root:
            return 0
        elif self.is_leaf(root):
            return 1
        return self.number_of_leaves(root.right) + self.number_of_leaves(root.left)

    #Time Complexity -- O(n)
    def number_of_non_leaves(self,root):
        if not root or self.is_leaf(root):
            return 0
        return 1 + self.number_of_non_leaves(root.left) + self.number_of_non_leaves(root.right)
    
    #Time Complexity -- O(n)
    def number_of_full_nodes(self,root):
        if not root or self.is_leaf(root):
            return 0
        elif root.right and root.left:
            return 1 + self.number_of_full_nodes(root.left) + self.number_of_full_nodes(root.right)
        return self.number_of_full_nodes(root.left) + self.number_of_full_nodes(root.right)