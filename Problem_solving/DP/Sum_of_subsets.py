''' Sum of Subsets -- It basically involves finding subsets of a given set in which sum of its elements 
is equal to specific target, if found then returns True/subset, if not then return False/-1.'''

#Time Complexity -- O(2^n)
def sum_of_subsets(array, target, index = 0, Sum = 0):
    if Sum == target:
        return True
    if index == len(array):
        return False
    return sum_of_subsets(array, target, index + 1, Sum + array[index]) or sum_of_subsets(array, target, index + 1, Sum)

#Time Complexity -- O(n * target)
#Space Complexity -- O(n * target)
def sum_of_subsets_dp(array, target, dp, index = 0, Sum = 0):
    if target == 0:
        return True
    if index == 0:
        dp = [[-1] * (target + 1) for _ in range(len(array) + 1)]
    if Sum == target:
        return True
    if Sum > target:
        return False
    if index == len(array):
        return False
    if dp[index][Sum] == 1:
        return True
    res = sum_of_subsets_dp(array, target, dp, index + 1, Sum + array[index]) or sum_of_subsets_dp(array, target, dp, index + 1, Sum)
    dp[index][Sum] = int(res)
    return res


    
