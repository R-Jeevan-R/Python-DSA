'''Minimum Operations required to equal the three numbered array with following operations.
1. Select any two numbers and add 1 to both of them.
2. Substract 1 from remaining number.
Return Minimum number of above operations to equal all three numbers and
return -1 if it is not possible to equal the give number by any possible number of operations.'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Algorithms.Sorting.Heap_sort import Heap_sort

#Time Complexity -- O(1) -- Becuase strictly 3 numbers are given, sorting takes O(1) time
def Minimum_number_of_opearions(array):
    array = Heap_sort(array)
    p , q, r = tuple(array)
    op1 = 0
    if (r - p)%2 != 0:
        return -1
    else:
        op1 += (r - p)//2
    p += op1
    q += op1
    r -= op1

    op2 = 0
    if (q - p)%2 != 0:
        return -1
    else:
        op2 += (q - p)//2
    p += op2
    q -= op2
    r += op2

    return op1 + op2


