import math

#Time Complexity -- O(d), where d -- Number of Digits
def Is_armstrong(number):
    Len = len(str(number))
    Sum = 0
    temp = number
    while number >= 1:
        Sum += math.pow((number%10),Len)
        number //= 10
    if Sum == temp:
        return True
    return False

#Time Complexity -- O(n*d), where d -- Number of Digits
def Armstrong_in_given_range(low=0,high=100):
    armstrongs = set()
    for i in range(low,high+1):
        Sum = 0
        temp = i
        while i!=0:
            Sum += math.pow((i%10),len(str(temp)))
            i = i // 10
        if Sum == temp:
            armstrongs.add(temp)
    return armstrongs










        
            
        
