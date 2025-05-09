''' Linked list is a Linear Data stucture stores elements in linearly singly connected nodes and
the start of list is pointed by head of linked list.'''

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        

class Linked_list():
    def  __init__(self):
        self.head=None

    #Time Complexity -- O(n)
    #Inserting a node at end of list
    def append(self,data):
        if not self.head:
            self.head=Node(data)
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        node=Node(data)
        temp.next=node

    #Time Complexity -- O(1)
    #Inserting a node at start of list
    def add(self,data):
        if not self.head:
            self.head=Node(data)
            return
        node=Node(data)
        node.next=self.head
        self.head=node

    #Time Complexity -- O(n)
    #Inserting a node at specified position
    def insert(self,data,position):
        if not self.head:
            if  position!=1:
                print("Inappropriate position to insert a node")
                return
            else:
                self.add(data)
                return
        temp=self.head
        for i in range(1,position-1):
            if not temp.next:
                print("Inappropriate position to insert a node")
                return
            temp=temp.next
        node=Node(data)
        node.next=temp.next
        temp.next=node
                
    #Time Complexity -- O(n)
    def print_list(self):
        if not self.head:
            print(None)
            return
        temp=self.head
        while temp:
            print(f"{temp.data} -->",end="")
            if temp.next:
                temp=temp.next
                continue
            break
        print("None")

    #Time Complexity -- O(1)
    def delete_from_beginning(self):
        if not self.head:
            print("Linked list is empty\n")
            return
        temp=self.head
        self.head=temp.next
        temp=None

    #Time Complexity -- O(n)
    def delete_from_end(self):
        if not self.head:
            print("Linked list is empty\n")
            return
        elif not self.head.next:
            self.head=None
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None