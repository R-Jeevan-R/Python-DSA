'''Binary Heap -- It is an Almost Complete Binary Tree.
Max Heap -- If at each node, the key of the node is greater than the values of its child nodes.
Min Heap -- If at each node, the key of the node is lower than the values of its child nodes.
'''
class Max_heap():
    def __init__(self,array):
        self.array=array
        self.heap_size=len(array)
        self.build_heap()

    #Time Complexity -- O(Logn)
    def heapify(self,i):
        left=2*i
        right=left+1
        if left<self.heap_size and self.array[left]>self.array[i]:
            largest=left
        else:
            largest=i
        if right<self.heap_size and self.array[right]>self.array[largest]:
            largest=right
        if largest!=i:
            self.array[largest],self.array[i]=self.array[i],self.array[largest]
            self.heapify(largest)

    #Time Complexity -- O(n)
    def build_heap(self):
        n=self.heap_size
        for i in range(n//2,-1,-1):
            self.heapify(i)

    #Time Complexity -- O(logn)
    def extract_max(self):
        if self.heap_size<1:
            print("Heap Underflow \n")
            return
        Max=self.array[0]
        self.array[0]=self.array[self.heap_size-1]
        self.heap_size-=1
        self.heapify(0)
        return Max

    #Time Complexity -- O(Logn)
    def insert_key(self,key):
        self.array.append(key)
        self.heap_size+=1
        i=self.heap_size-1
        while ( i>0 and self.array[i//2] < self.array[i]):
            self.array[i],self.array[i//2]=self.array[i//2],self.array[i]
            i=i//2

    #Time Complexity -- O(1)
    def find_max(self):
        if self.heap_size<1:
            print("Heap Underflow \n")
            return
        Max=self.array[0]
        self.array[0]=self.array[self.heap_size-1]
        self.heap_size-=1
        self.heapify(0)
        return Max

    #Time Complexity -- O(Logn)
    def insert_key(self,key):
        self.array.append(key)
        self.heap_size+=1
        i=self.heap_size-1
        while ( i>0 and self.array[i//2] < self.array[i]):
            self.array[i],self.array[i//2]=self.array[i//2],self.array[i]
            i=i//2

    #Time Complexity -- O(1)
    def find_max(self):
        return self.array[0]

