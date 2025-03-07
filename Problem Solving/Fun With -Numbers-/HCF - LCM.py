def HCF(numbers):
    small = min(numbers)
    for i in range(small,0,-1):
        flag = 0
        for number in numbers:
            if number % i != 0:
                flag = 1
                break
        if flag == 0:
            return i

def LCM(numbers):
    Max = max(numbers)
    while True:
        flag = 0
        for number in numbers:
            if Max % number != 0:
                flag = 1
                break
        if flag == 0:
            return Max
        Max += 1
            

    
    
