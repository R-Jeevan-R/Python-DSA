'''Binary Heap -- It is an Almost Complete Binary Tree.
Max Heap -- If at each node, the key of the node is greater than the values of its child nodes.
Min Heap -- If at each node, the key of the node is lower than the values of its child nodes.
'''
class Max_heap():
    def __init__(self, array):
        self.array = array
        self.heap_size = len(array)
        self.build_heap()

    # Time Complexity -- O(log n)
    def heapify(self, i):
        left = 2 * i + 1 
        right = 2 * i + 2  
        largest = i

        if left < self.heap_size and self.array[left] > self.array[largest]:
            largest = left
        if right < self.heap_size and self.array[right] > self.array[largest]:
            largest = right
        if largest != i:
            self.array[largest], self.array[i] = self.array[i], self.array[largest]
            self.heapify(largest)

    # Time Complexity -- O(n)
    def build_heap(self):
        n = self.heap_size
        for i in range((n // 2) - 1, -1, -1):  
            self.heapify(i)

    # Time Complexity -- O(log n)
    def extract_max(self):
        if self.heap_size < 1:
            print("Heap Underflow \n")
            return None
        Max = self.array[0]
        self.array[0] = self.array[self.heap_size - 1]
        self.array.pop()  
        self.heap_size -= 1
        self.heapify(0)
        return Max

    # Time Complexity -- O(log n)
    def insert_key(self, key):
        self.array.append(key)
        self.heap_size += 1
        i = self.heap_size - 1

        while i > 0 and self.array[(i - 1) // 2] < self.array[i]:  
            parent = (i - 1) // 2
            self.array[i], self.array[parent] = self.array[parent], self.array[i]
            i = parent

    # Time Complexity -- O(1)
    def find_max(self):
        if self.heap_size > 0:
            return self.array[0]  
        return None

class Min_heap():
    def __init__(self,array):
        self.array = array
        self.heap_size = len(array)
        self.build_heap()

    # Time Complexity -- O(n)
    def build_heap(self):
        n = self.heap_size
        for i in range((n // 2) - 1, -1, -1):  
            self.heapify(i)
    
    # Time Complexity -- O(log n)
    def heapify(self, i):
        left = 2 * i + 1 
        right = 2 * i + 2  
        smallest = i

        if left < self.heap_size and self.array[left] < self.array[smallest]:
            smallest = left
        if right < self.heap_size and self.array[right] < self.array[smallest]:
            smallest = right
        if smallest != i:
            self.array[smallest], self.array[i] = self.array[i], self.array[smallest]
            self.heapify(smallest)
    
    # Time Complexity -- O(log n)
    def extract_min(self):
        if self.heap_size < 1:
            print("Heap Underflow \n")
            return None
        Min = self.array[0]
        self.array[0] = self.array[self.heap_size - 1]
        self.array.pop()  
        self.heap_size -= 1
        self.heapify(0)
        return Min
    
    # Time Complexity -- O(log n)
    def insert_key(self, key):
        self.array.append(key)
        self.heap_size += 1
        i = self.heap_size - 1

        while i > 0 and self.array[(i - 1) // 2] > self.array[i]:  
            parent = (i - 1) // 2
            self.array[i], self.array[parent] = self.array[parent], self.array[i]
            i = parent
    
    # Time Complexity -- O(1)
    def find_min(self):
        if self.heap_size > 0:
            return self.array[0]  
        return None

    



