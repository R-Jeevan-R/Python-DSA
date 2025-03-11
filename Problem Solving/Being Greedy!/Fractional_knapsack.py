import sys
import os

# Dynamically adds the project root (Python-DSA) to Python's module search path.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Algorithms.Sorting.Heap_sort import Heap_sort #Refer Heap_sort in Sorting Algorithms

#Time Complexity -- O(nlogn)
def Fractional_knapsack(number_of_items,weights,profits,capacity):
    #Verifying if info about items is perfectly matching before proceeding further
    if (number_of_items != len(weights)) or (number_of_items != len(profits)):
        print('Number of items and corresponding weights or profits are not matching!')
        return
    
    #Calculating Profit to Weight ratios
    profit_to_weight = []
    for i in range(number_of_items):    #O(n)
        profit_to_weight.append((round(profits[i]/weights[i],2),i))
    
    #Sorting Profit to Weight Ratios (Greedy About P/W Ratios) #O(nlogn)
    profit_to_weight = Heap_sort(profit_to_weight,asc = False)
    
    #Calculating Maximum Profit
    max_profit = 0
    for pw , i in profit_to_weight:     #O(n)
        if capacity > 0 and weights[i] <= capacity :
            capacity -= weights[i]
            max_profit += profits[i]
        else:
            break
    
    #Adding the Fractional Profit at Last
    if capacity > 0:
        max_profit += pw*capacity

    return max_profit
