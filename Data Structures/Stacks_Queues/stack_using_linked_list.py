class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack():
    def __init__(self):
        self.top=None
        
    def push(self,element):
        node=Node(element)
        node.next=self.top
        self.top=node

    def pop(self):
        if not self.top:
            print("Stack underflow\n")
            return
        p=self.top.data
        self.top=self.top.next
        return p

    def is_empty(self):
        if not self.top:
            return True
        return False

    def seek(self):
        if self.is_empty():
            print("Stack is empty\n")
            return 
        return self.top.data

    def print_stack(self):
        if not self.top:
            print("Stack is empty\n")
            return
        temp=self.top
        while temp:
            print(f"{temp.data}")
            temp=temp.next


