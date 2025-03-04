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
    
    
