import math
#Time Complexity -- O(nlogn)
def Primes(lower,upper):
    if lower > upper :
        return "Specify interval correctly!"
    primes=[]
    for num in range(lower,upper+1):
        if num==1:
            continue
        flag=0
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                flag=1
                break
        if flag==0:
            primes.append(num)
    return primes
    
        
