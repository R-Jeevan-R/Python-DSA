''' Insertion Sort -- Maintains Two sub Lists, one is sorted and other is unsorted
Time Complexity -- O(n) to O(n^2)
Space Complexity -- O(1)
Inplace algorithm -- No extra space required'''
def Insertion_sort(List):
    for i in range(1,len(List)):
        key=List[i]
        j=i-1
        while j>=0 and key<List[j] :
            List[j+1]=List[j]
            j-=1
        List[j+1]=key
        
