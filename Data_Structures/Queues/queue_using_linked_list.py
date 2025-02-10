'''Queue -- FIFO(Fisrt-In First-Out) Linear Data structure.
Implementing a queue using a linked list will store elements linearly
but not necessarily in contigous memory locations.
Addition of an element is done at the end of linked list where as
Deletion of elemets is done at the head(start) of list.'''

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue():
    def __init__(self):
        self.front=None
        self.rear=None

    #Time Complexity -- O(1)
    def enqueue(self,data):
        node=Node(data)
        if not self.front:
            self.front=node
            self.rear=node
            return
        self.rear.next=node
        self.rear=node

    #Time Complexity -- O(1)
    def dequeue(self):
        if self.is_empty():
            print("Queue underflow\n")
            return
        elif self.front==self.rear:
            d=self.front.data
            self.front=self.rear=None
            return d
        d=self.front.data
        self.front=self.front.next
        return d

    #Time Complexity -- O(1)
    def is_empty(self):
        if not self.front:
            return True
        return False

    #Time Complexity -- O(n)
    def print_queue(self):
        if self.is_empty():
            print("Queue is empty\n")
            return
        temp=self.front
        while temp!=self.rear:
            print(temp.data,end='->')
            temp=temp.next
        print(temp.data,end='->')
        print(None)

            
        
