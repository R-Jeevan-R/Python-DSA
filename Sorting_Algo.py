'''Bubble Sort -- Pairwise comparison of adjacent elements
Time Complexity -- O(n) to O(n^2)
Inplace algorithm -- No Extra Space Required'''
def Bubble_sort(List):
    for i in range(0,len(List)):
        flag=False
        for j in range(0,len(List)-i-1):
            if List[j]>List[j+1]:
                List[j+1],List[j]=List[j],List[j+1]
                flag=True
        if not(flag):
            break


        
'''Selection Sort -- Finding Minimum element at each iteration and placing it in its position
Time Complexity -- Theta(n)
Inplace algorithm'''
def selection_sort(List):
    for i in range(0,len(List)):
        min_index=i
        for j in range(i+1,len(List)):
            if List[j]<List[min_index]:
                min_index=j
        if min_index!=i:
            List[min_index],List[i]=List[i],List[min_index]



''' Insertion Sort -- Maintains Two sub Lists, one is sorted and other is unsorted
Time Complexity -- O(n) to O(n^2)
Inpllace algorithm'''
def insertion_sort(List):
    for i in range(1,len(List)):
        key=List[i]
        j=i-1
        while j>=0 and key<List[j] :
            List[j+1]=List[j]
            j-=1
        List[j+1]=key
        

'''Merge Sort -- Follows Divide and Conquer Appraoch, Recursively divides the List into two havles and finally merges them
in sorted order
Time Complexity -- Theta(nlogn)
Space Complexity -- O(n)
Out of place algorithm'''
def merge_sort(low,high,List):
    if low==high:
        return
    mid=(low+high)//2
    merge_sort(low,mid,List)
    merge_sort(mid+1,high,List)
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



'''Quick Sort -- Recursively chose a pivot element(specific) and place it in its position i.e all elements left of it are less than
its value and all elements right of it greater than its value.
Time complexity -- O(nlogn) to O(n^2)
Space Complexity --O(logn)'''
def quick_sort(low,high,List):
    if low<=high:
        p=partition(low,high,List)
        quick_sort(low,p-1,List)
        quick_sort(p+1,high,List)

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
    
    
            

    
if __name__=='__main__':
    L=[5,4,4,4,3,2,2,1,1]
    print("Before sortig : ",L)
    c=quick_sort(0,len(L)-1,L)
    print("After Sorting : ",L)
    print("Number od shifts : ",c)
            

            
            
