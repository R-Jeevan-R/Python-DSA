class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue():
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,data):
        node=Node(data)
        if not self.front:
            self.front=node
            self.rear=node
            return
        self.rear.next=node
        self.rear=node

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

    def is_empty(self):
        if not self.front:
            return True
        return False

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

            
        
