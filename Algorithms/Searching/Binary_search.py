'''Binary Search -- Follows divide and conquer approach and requires list
to be sorted
Time Complexity --Theta(logn)
Space complexity -- O(1)'''
def Binary_search(List,key):
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


'''Recursive binary Search -- Follows divide and conquer approach and requires list
to be sorted
Time Complexity --Theta(logn)
Space complexity -- O(logn)'''
def Recursive_binary_search(List,key,low,high):
    if low>high:
        return False
    mid=(low+high)//2
    if List[mid]==key:
        return True
    elif List[mid]>key:
        Recursive_binary_search(List,key,low,mid-1)
    else:
        Recursive_binary_search(List,key,mid+1,high)
    
