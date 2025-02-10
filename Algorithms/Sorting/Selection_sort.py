'''Selection Sort -- Finding Minimum element at each iteration and placing it in its position
Time Complexity -- Theta(n^2)
Space Complexity -- O(1)
Inplace algorithm -- No extra space required'''
def Selection_sort(List):
    for i in range(0,len(List)):
        min_index=i
        for j in range(i+1,len(List)):
            if List[j]<List[min_index]:
                min_index=j
        if min_index!=i:
            List[min_index],List[i]=List[i],List[min_index]

