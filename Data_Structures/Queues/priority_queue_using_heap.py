'''Priority Queue -- A Special type of queue where elements in the queue are dequeued based on
priority not just on FIFO order.'''

from Binary_heaps import Max_heap

class Priority_queue():
    def __init__(self):
        self.heap=Max_heap([])
        
    #Time Complexity -- O(logn)
    def priority_enqueue(self,element):
        self.heap.insert_key(element)

    #Time Complexity -- O(logn)
    def priority_dequeue(self):
        return self.heap.extract_max()

