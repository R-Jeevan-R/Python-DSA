import math

#Time Complexity -- O(n^(1/2))
def Is_prime(number):
    if number<=1:
        print("Try to enter Natural Numbers > 1!")
        return
    for i in range(2,int(math.sqrt(number))+1):
        if number%i==0:
            return False
    return True

    
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


    
        
