'''Fibonacci Sequence -- Starts with 0 and 1, and each number in sequence
is obtained bu adding previous two numbers.'''

class Fibonacci():

    #Time Complexity -- O(2^n) -- Can be Optimized using Dynamic Programming
    def fibo_series_using_recursion(self,n):
        def helper(n):
            if n==0:
                return 0
            elif n==1:
                return 1
            return helper(n-1) + helper(n-2)
        
        series = []
        for i in range(n):
            series.append(helper(i))
        return series
    
    #Time Complexity -- O(n)
    def fibo_series_using_iteration(self,n):
        series = []
        for i in range(n):
            if i==0 or i==1:
                series.append(i)
                continue
            series.append(series[i-1]+series[i-2])
        return series
    
    #Time Complexity -- O(n)
    def nth_number_in_fibo_series(self,n):
        return self.fibo_series_using_iteration(n)[-1]
        
        
            
            
        
        
        
