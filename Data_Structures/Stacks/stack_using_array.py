'''Stack -- LIFO(Last-In First-Out) Linear Data structure.
Implementing stack using an array stores elements in contingous memory
locations and addition as well as deletion of an element is done at the end of array.'''

class Stack():
    def __init__(self,max_size):
        self.max_size=max_size
        self.stack=[float('inf')]*self.max_size
        self.num_of_elements=0
        self.top=-1

    #Time Complexity -- O(1)
    def push(self,element):
        if self.is_Full():
            print("Stack Overflow\n")
            return
        else:
            self.top+=1
            self.num_of_elements+=1
            self.stack[self.top]=element
            return
        
    #Time Complexity -- O(1)
    def pop(self):
        if self.is_Empty():
            print("Stack underflow\n")
            return None
        else:
            p=self.stack[self.top]
            self.num_of_elements-=1
            self.stack[self.top]=float('inf')
            self.top-=1
            return p
        
    #Time Complexity -- O(1)
    def is_Empty(self):
        if self.top==-1:
            return True
        return False
    
    #Time Complexity -- O(1)
    def is_Full(self):
        if self.top+1==self.max_size:
            return True
        return False

    #Time Complexity -- O(1)
    def seek(self):
        if self.is_empty():
            print("Stack is Empty\n")
            return None
        return self.stack[self.top]

    #Time Complexity -- O(n)
    def print_stack(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])