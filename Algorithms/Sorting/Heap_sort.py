'''Heap_Sort: It uses heap and recursively or iteratively extract min or max key.'''

import sys
import os

# Dynamically adds the project root (Python-DSA) to Python's module search path.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Data_Structures.Binary_trees.Heaps import * #Refer Heaps in Binary Trees in Data Structures
#Time Complexity -- O(nlogn)
def Heap_sort(array, asc=True):

    #Max_heap for non-decreasing order
    if asc == True :
        h = Max_heap(array)
    
    #Min_heap for non-increasing order
    else:
        h = Min_heap(array)
    n=len(array)
    for i in range(n-1,0,-1):
        h.array[0],h.array[i]=h.array[i],h.array[0]
        h.heap_size-=1
        h.heapify(0)
    return array
