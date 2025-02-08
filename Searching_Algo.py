from Sorting_Algo import quick_sort
'''Linear Search -- Perform element comparison iteratively
Time Complexity --O(n)
Space Complexity -- O(1)'''
def linear_search(List,key):
    for el in List:
        if  el==key:
            return True
    return False


'''Binary Search -- Follows divide and conquer approach and requires list to be sorted
Time Complexity --Theta(logn)
Space complexity -- O(1){Using iteration}
                                  O(logn){Using recurion}'''
def Binary_search(List,key):
    quick_sort(0,len(List)-1,List)
    low=0
    high=len(List)-1
    while(low<=high):
        mid=(low+high)//2
        if List[mid]==key:
            return True
        elif List[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return False



'''Bitonic Search -- List should have an index upto which list is in ascending(or Descending) order and then
decreases(or increases).
Time Complexity -- O(logn)
Space Complexity -- O(1){Using Iteration}
                                   O(logn){Using Recursion}'''
def Bitonic_search(List,index,key):
    if Binary_search(List[:index+1],key) or Binary_search(List[index+1:],key) :
        return True
    else:
        return False
    

