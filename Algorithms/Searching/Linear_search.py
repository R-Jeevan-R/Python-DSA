'''Linear Search -- Perform element comparison iteratively
Time Complexity --O(n)
Space Complexity -- O(1)'''

def Linear_search(List,key):
    for el in List:
        if  el==key:
            return True
    return False

'''Recursive Linear Search -- Perform element comparison recursively
Time Complexity --O(n)
Space Complexity -- O(n)'''

def Recursive_linear_search(List,index,key):
    if index==len(List):
        return False
    elif List[index]==key:
        return True
    Recursive_linear_search(List,index+1,key)


    
