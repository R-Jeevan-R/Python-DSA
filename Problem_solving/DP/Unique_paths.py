''' Unique paths -- This Problem is basically a puzzle which is a M*N grid wiht start and finish cells.
One can move one cell Right or Down at once from start position.
It is to count number of unique paths are possible to reach Finish cell(I,J) from Start(i,j).'''


#Time Complexity -- O(M*N)
#Space Complexity -- O(M*N)
def Unique_paths_dp(i, j, s, dp):
    if (i,j) == s:
        return 1
    if i<0 or j<0 :
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    up = Unique_paths(i - 1, j, s, dp)
    left = Unique_paths(i, j - 1, s, dp)
    dp[i][j] = up + left 
    return dp[i][j]

#Time Complexity -- O(2^(M+N))
#Space Complexity -- O(M+N)
def Unique_paths(i, j):
    if (i,j) == (0,0):
        return 1
    if i < 0 or j < 0 :
        return 0
    left = Unique_paths(i, j - 1)
    right = Unique_paths(i - 1, j)
    return left + right


def Number_of_unique_paths(rows, columns ,start = (1,1), finish = None):
    if finish is None:
        finish = (rows, columns)
    dp = [[-1]*columns for _ in range(rows)]
    start = (start[0] - 1, start[1] - 1)
    number = Unique_paths_dp(finish[0] - 1, finish[1] - 1, start, dp) #Using Dynamic Programming
    # number = Unique_paths(finish[0] - 1, finish[1] - 1) #Using Brute Force Recursion
    return number


