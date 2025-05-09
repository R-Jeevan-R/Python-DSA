'''Circular queue -- FIFO(First-In First-Out) linear Data structure.
Implementing a circular queue using an array will store elements in contigous
memory locations and in circular fashion.
Reuses empty spaces left after dequeuing, whereas a normal queue may lead to wasted space.
Addition of element is done at start of array whereas
Deletion of an element is done at end of array. '''

class queue():
    def __init__(self,max_size):
        self.front=-1
        self.rear=-1
        self.max_size=max_size
        self.queue=[float('inf')]*self.max_size

    #Time Complexity -- O(1)
    def enqueue(self,element):
        if self.is_full():
            print("Queue Overflow\n")
            return
        elif self.front==-1:
            self.front+=1
            self.rear+=1
            self.queue[self.rear]=element
            return
        else:
            self.rear=(self.rear+1)%self.max_size
            self.queue[self.rear]=element
            return

    #Time Complexity -- O(1)
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow\n")
            return
        elif self.front==self.rear:
            d=self.queue[self.front]
            self.queue[self.front]=float('inf')
            self.front=-1
            self.rear=-1
            return d
        else:
            d=self.queue[self.front]
            self.queue[self.front]=float('inf')
            self.front=(self.front+1)%self.max_size
            return d
        
    #Time Complexity -- O(1)
    def is_empty(self):
        if self.front==-1:
            return True
        return False

    #Time Complexity -- O(1)
    def is_full(self):
        if (self.rear+1)%self.max_size==self.front:
            return True
        return False
    
    #Time Complexity -- O(n)
    def print_queue(self):
        if self.rear>self.front:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=' ')
        else:
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            for i in range(self.front,self.max_size):
                print(self.queue[i],end=" ")
        print()