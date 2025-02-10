class Stack():
    stack=[]
    top=0
    max_size=0
    def __init__(self,max_size):
        self.max_size=max_size
        self.stack=[float('inf')]*self.max_size
        self.top=-1
        
    def push(self,element):
        if self.is_Full():
            print("Stack Overflow\n")
            return
        else:
            self.top+=1
            self.stack[self.top]=element
            return
        
    def pop(self):
        if self.is_Empty():
            print("stack underflow\n")
            return None
        else:
            p=self.stack[self.top]
            self.stack[self.top]=float('inf')
            self.top-=1
            return p

    def is_Empty(self):
        if self.top==-1:
            return True
        return False

    def is_Full(self):
        if self.top+1==self.max_size:
            return True
        return False

    def seek(self):
        if self.is_empty():
            print("Stack is Empty\n")
            return None
        return self.stack[self.top]

    def print_stack(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])






    
