'''Tree Traversal algorithms:
Inorder -- (Left, Root, Right)
Preorder -- (Root, Left, Right)
Postorder -- (Left, Right, Root)
'''

class Traversals:
    def __init__(self):
        pass

    # Time Complexity: O(n)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    # Time Complexity: O(n)
    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    # Time Complexity: O(n)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')
