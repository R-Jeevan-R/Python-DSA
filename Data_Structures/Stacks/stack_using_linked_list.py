''' Stack -- LIFO(Last-In First-Out) linear Data structure. Implementing
stack using a Linked list will store elements linearly but not
necessirily in contigous memory locations and addition as well as
deletion of elements of elements is done at the head(start) of linked list.'''

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Stack():
    def __init__(self):
        self.top=None

    #Time Complexity -- O(1)   
    def push(self,element):
        node=Node(element)
        node.next=self.top
        self.top=node

    #Time Complexity -- O(1)
    def pop(self):
        if not self.top:
            print("Stack underflow\n")
            return
        p=self.top.data
        self.top=self.top.next
        return p

    #Time Complexity -- O(1)
    def is_empty(self):
        if not self.top:
            return True
        return False

    #Time Complexity -- O(1)
    def seek(self):
        if self.is_empty():
            print("Stack is empty\n")
            return 
        return self.top.data

    #Time Complexity -- O(n)
    def print_stack(self):
        if not self.top:
            print("Stack is empty\n")
            return
        temp=self.top
        while temp:
            print(f"{temp.data}")
            temp=temp.next


