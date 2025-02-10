'''Bubble Sort -- Pairwise comparison of adjacent elements
Time Complexity -- O(n) to O(n^2)
Space Complexity - O(1)
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


       
