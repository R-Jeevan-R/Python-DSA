'''Sum _of_sub_arrays -- This problem is involves finding out all subarrays(not subsets) in an array of integers
which sums to given target.'''

#Time Complexity -- O(n^2)
def Sum_of_sub_arrays(array,target):
    sub_arrays = []
    for i in range(len(array)):
        cur_sum = 0
        for j in range(i, len(array)):
            cur_sum += array[j]
            if cur_sum == target:
                sub_arrays.append(array[i:j+1])
    return sub_arrays


#Time Complexity -- O(n) to O(n^2)
def Optimized_sum_of_sub_arrays(array,target):
    sub_arrays = []
    Map = dict()
    cur_sum = 0
    for i in range(len(array)):
        cur_sum += array[i]
        if cur_sum == target:
            sub_arrays.append(array[:i+1])
        if (cur_sum - target) in Map :
            for start_index in Map[cur_sum - target]:
                sub_arrays.append(array[start_index+1:i+1])
        if cur_sum not in Map :
            Map[cur_sum] = [i]
        else:
            Map[cur_sum].append(i)
        
    return sub_arrays

    
