'''Queue -- FIFO(FIsrt-In Fisrt-Out) linear Data structure.
Implementing a queue using an array will store elements in contigous memroy locations.
Addition of elements is done at start of array where as Deletion of elements
is done at the end of array.'''

class Queue():
    def __init__(self,max_size):
        self.front=-1
        self.rear=-1
        self.max_size=max_size
        self.queue=[float('inf')]*self.max_size
        self.num_of_elements=0

    #Time Complexity -- O(1)
    def enqueue(self,element):
        if self.is_full():
            print("Queue Overflow\n")
            return
        elif self.front==-1:
            self.front+=1
            self.rear+=1
            self.queue[self.rear]=element
            self.num_of_elements+=1
            return
        else:
            self.rear+=1
            self.queue[self.rear]=element
            self.num_of_elements+=1
            return

    #Time Complexity -- O(n)
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow\n")
            return
        elif self.front==self.rear:
            d=self.queue[self.front]
            self.queue[self.front]=float('inf')
            self.front=-1
            self.rear=-1
            self.num_of_elements-=1
            return d
        else:
            d=self.queue[self.front]
            i=0
            while i<self.rear:
                self.queue[i]=self.queue[i+1]
                i+=1
            self.rear=i-1
            while i<self.max_size:
                self.queue[i]=float('inf')
                i+=1
            self.num_of_elements-=1
            return d

    #Time Complexity -- O(1)
    def is_empty(self):
        if self.front==-1:
            return True
        return False

    #Time Complexity -- O(1)
    def is_full(self):
        if self.rear+1==self.max_size:
            return True
        return False
    
    #Time Complexity -- O(n)
    def print_queue(self):
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=' ')
        print()