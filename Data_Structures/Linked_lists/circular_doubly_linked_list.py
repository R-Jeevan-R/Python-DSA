''' Circular Doubly Linked list stores elements in linearly doubly
connected nodes and every node maintains two pointers next and prev.
And also the last and first nodes are connected to each other.
Start of the linked list is pointed by head pointer.'''
class Node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Circular_doubly_linked_list():
    def __init__(self):
        self.head=None

    #Time Complexity -- O(1)
    #Inserting a node at end of list
    def append(self,element):
        node=Node(element)
        if not self.head:
            self.head=node
            self.head.next=self.head
            self.head.prev=self.head
            return
        last=self.head.prev
        node.next=last.next
        node.prev=last
        self.head.prev=node
        last.next=node
        
        
    #Time Complexity -- O(1)
    #Inserting a node at start of list
    def add(self,element):
        node=Node(element)
        if not self.head:
            self.head=node
            self.head.next=self.head
            self.head.prev=self.head
            return
        last=self.head.prev
        last.next=node
        node.prev=last
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
        last=self.head.prev
        print(f"{temp.data}",end="<-->")
        while temp.next!=last:
            temp=temp.next
            print(f"{temp.data}",end="<-->")
        print(f"{last.data}")
            
    #Time Complexity -- O(n)
    def print_reversed_list(self):
        if not self.head:
            print(None)
            return
        last=self.head.prev
        while last!=self.head:
            print(f"{last.data}",end='<-->')
            last=last.prev
        print(f"{self.head.data}")

    #Time Complexity -- O(1)
    def delete_from_beginning(self):
        if not self.head:
            print("Circular doubly linked list is empty\n")
            return
        elif not self.head.next:
            self.head=None
            return
        temp=self.head
        self.head=temp.next
        temp.prev.next=self.head
        self.head.prev=temp.prev
        temp=None

    #Time Complexity -- O(1)
    def delete_from_end(self):
        if not self.head:
            print("Doubly linked list is empty\n")
            return
        elif not self.head.next:
            self.head=None
            return
        temp=self.head.prev.prev
        temp.next.prev=None
        temp.next.next=None
        temp.next=self.head
        self.head.prev=temp
