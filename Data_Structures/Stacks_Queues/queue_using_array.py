class queue():
    queue=[]
    front=rear=0
    max_size=0
    def __init__(self,max_size):
        self.front=-1
        self.rear=-1
        self.max_size=max_size
        self.queue=[float('inf')]*self.max_size

    def enqueue(self,element):
        if self.rear+1==self.max_size:
            print("Queue Overflow\n")
            return
        elif self.front==-1:
            self.front+=1
            self.rear+=1
            self.queue[self.rear]=element
            return
        else:
            self.rear+=1
            self.queue[self.rear]=element
            return

        
    def dequeue(self):
        if self.front==-1:
            print("Queue Underflow\n")
            return
        elif self.front==self.rear:
            d=self.queue[self,front]
            self.queue[self.front]=float('inf')
            self.front=-1
            self.rear=-1
            return d
        else:
            d=self.queue[self.front]
            self.queue[self.front]=float('inf')
            self.front+=1
            return d

    def print_queue(self):
        for i in range(self.front,self.rear+1):
            print(self.queue[i],end=' ')
        


        
