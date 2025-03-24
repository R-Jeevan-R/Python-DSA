''' Job Sequencing with Deadlines -- It is an Optimization problem where the given jobs
with respective deadlines needs to be scheduled to achieve Maximum profit.'''

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Algorithms.Sorting.Heap_sort import Heap_sort

#Time Complexity -- max(O(nlogn), O(n * max_deadline))
#Space Complexity -- O(max_deadline)

def Job_sequecing(jobs):
    jobs = Heap_sort(jobs, asc = False) #O(nlogn)
    max_deadline = 0
    for _, deadline, _ in jobs: #O(n)
        if max_deadline < deadline :
            max_deadline = deadline
    array = [None] * max_deadline
    for profit, deadline, name in jobs: #O(n * max_deadline)
        if not array[deadline - 1]:
            array[deadline - 1] = (name, profit)
        else:
            for i in range(deadline - 1, -1, -1):   #O(max_deadline)
                if not array[i]:
                    array[i] = (name, profit)
                    break
    max_profit = sum([job[1] for job in array if job])
    return max_profit, array
