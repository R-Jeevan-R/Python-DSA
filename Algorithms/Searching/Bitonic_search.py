'''Bitonic Search -- List should have an index upto which list is in ascending(or Descending) order and then
decreases(or increases).
Time Complexity -- O(logn)
Space Complexity -- O(1){Using Iteration} O(logn){Using Recursion}'''
def Bitonic_search(List,index,key):
    if Binary_search(List[:index+1],key) or Binary_search(List[index+1:],key) :
        return True
    else:
        return False
