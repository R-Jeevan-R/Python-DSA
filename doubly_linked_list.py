class Node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class Doubly_linked_list():
    def __init__(self):
        self.head=None

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

    def add(self,element):
        if not self.head:
            self.head=Node(element)
            return
        node=Node(element)
        node.next=self.head
        self.head.prev=node
        self.head=node

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


        
    
