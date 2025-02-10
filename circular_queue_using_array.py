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
        if (self.rear+1)%self.max_size==self.front:
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
            self.front=(self.front+1)%self.max_size
            return d
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



