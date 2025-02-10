'''Quick Sort -- Recursively chose a pivot element(specific) and place it in its position i.e all elements left of it are less than
its value and all elements right of it greater than its value.
Time complexity -- O(nlogn) to O(n^2)
Space Complexity --O(logn)
Outof Place algorithm -- Requires extra space'''
def Quick_sort(low,high,List):
    if low<=high:
        p=partition(low,high,List)
        Quick_sort(low,p-1,List)
        Quick_sort(p+1,high,List)

def partition(low,high,List):
    #Choosing rightmost element as Pivot element
    pivot=List[high]
    j=high-1
    i=low-1
    while i<=j and List[i+1]<pivot:
        i+=1
    while j>i:
        if List[j]<pivot:
            List[i+1],List[j]=List[j],List[i+1]
            i+=1
        j-=1
    List[i+1],List[high]=List[high],List[i+1]
    return i+1
    
    
