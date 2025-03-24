import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Data_Structures.Binary_trees.Heaps import *

#Time Complexity -- O(n),  Becuase k is some constant.
def kthlargest(array, k):
    if k <= 0 or k >= len(array):
        print('Index out of range')
        return
    heap = Max_heap(array)  #O(n)
    temp = []

    for _ in range(k - 1):  #O(klogn)
        temp.append(heap.extract_max()) #O(logn)

    value = heap.find_max() #O(1)

    for el in temp: #O(klogn)
        heap.insert_key(el) #O(logn)

    return value

#Time Complexity -- O(n),  Becuase k is some constant.
def kthsmallest(array, k):
    if k <= 0 or k >= len(array):
        print('Index out of range')
        return
    
    heap = Min_heap(array)  #O(n)
    temp = []

    for _ in range(k - 1):  #O(klogn)
        temp.append(heap.extract_min()) #O(logn)
    
    value = heap.find_min() #O(1)

    for el in temp: #O(klogn)
        heap.insert_key(el) #O(logn)
    
    return value

    