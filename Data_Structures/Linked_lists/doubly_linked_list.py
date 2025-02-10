''' Doubly Linked list stores elements in linearly doubly connected nodes and
every node maintains two pointers next and prev.
Start of the linked list is pointed by head pointer.'''

class Node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Doubly_linked_list():
    def __init__(self):
        self.head=None

    #Time Complexity -- O(n)
    #Inserting a node at end of list
    def append(self,element):
        node=Node(element)
        if not self.head:
            self.head=node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        node.prev=temp
        temp.next=node

    #Time Complexity -- O(1)
    #Inserting a node at start of list
    def add(self,element):
        if not self.head:
            self.head=Node(element)
            return
        node=Node(element)
        node.next=self.head
        self.head.prev=node
        self.head=node
        
    #Time Complexity -- O(n)
    #Inserting a node at specified position
    def insert(self,element,position):
        if not self.head:
            if  position!=1:
                print("Inappropriate position to insert a node")
                return
            else:
                self.add(element)
                return
        temp=self.head
        for i in range(1,position-1):
            if not temp.next:
                print("Inappropriate position to insert a node")
                return
            temp=temp.next
        node=Node(element)
        node.next=temp.next
        if temp.next:
            temp.next.prev=node
        temp.next=node
        node.prev=temp
        
    #Time Complexity -- O(n)
    def print_list(self):
        if not self.head:
            print(None)
            return
        temp=self.head
        while temp:
            print(f"{temp.data}<-->",end="")
            if temp.next:
                temp=temp.next
                continue
            break
        print("None")
        
    #Time Complexity -- O(n)
    def print_reversed_list(self):
        if not self.head:
            print(None)
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(f"{temp.data}<-->",end="")
            if temp.prev:
                temp=temp.prev
                continue
            break
        print("None")

    #Time Complexity -- O(1)
    def delete_from_beginning(self):
        if not self.head:
            print("Doubly linked list is empty\n")
            return
        elif not self.head.next:
            self.head=None
            return
        temp=self.head
        self.head=temp.next
        temp=None
        self.head.prev=temp

    #Time Complexity -- O(n)
    def delete_from_end(self):
        if not self.head:
            print("Doubly linked list is empty\n")
            return
        elif not self.head.next:
            self.head=None
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None


        
    
