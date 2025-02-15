'''Counting Sort -- It is used when the range of numbers are known.
Time Complexity -- O(n+K), where N- Number of elements and K- Hash Map Size.
Space Complexity -- O(K)
Out of Place algortihm -- Requires extra space'''

def Counting_sort(List,Min,Max):
    Dict=dict()
    for i in range(Min,Max+1):
        Dict[i]=0
    for el in List:
        Dict[el]+=1
    List=list()
    for i in range(Min,Max+1):
        if Dict[i]!=0:
            List.extend([i]*Dict[i])
    return List
