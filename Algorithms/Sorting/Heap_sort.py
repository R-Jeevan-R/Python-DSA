'''Heap_Sort: It uses heap and recursively or iteratively extract min or max key.'''

from Data_Structures.Binary_trees.Max_heap import Max_heap
def Heap_sort(array):
    h=Max_heap(array)
    n=len(array)
    for i in range(n-1,0,-1):
        h.array[0],h.array[i]=h.array[i],h.array[0]
        h.heap_size-=1
        h.heapify(0)

