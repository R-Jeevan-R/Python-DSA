'''Merge Sort -- Follows Divide and Conquer Appraoch, Recursively divides the List into two havles and finally merges them
in sorted order
Time Complexity -- Theta(nlogn)
Space Complexity -- O(n)
Out of place algorithm -- Requires extra space'''
def Merge_sort(low,high,List):
    if low==high:
        return
    mid=(low+high)//2
    Merge_sort(low,mid,List)
    Merge_sort(mid+1,high,List)
    merge(low,mid,high,List)
def merge(low,mid,high,List):
    left=[]
    right=[]
    l1=mid-low+1
    l2=high-mid
    for i in range(low,mid+1):
        left.append(List[i])
    for j in range(mid+1,high+1):
        right.append(List[j])

    i=j=0
    k=low
    while i<l1 and j<l2:
        if left[i]<=right[j]:
            List[k]=left[i]
            i+=1
            k+=1
        else:
            List[k]=right[j]
            j+=1
            k+=1
    while i<l1:
        List[k]=left[i]
        i+=1
        k+=1
    while j<l2:
        List[k]=right[j]
        k+=1
        j+=1

