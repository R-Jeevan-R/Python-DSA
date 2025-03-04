#Time Complexity -- O(n)
#Space Complexity  -- O(1) or O(n) based on Implementation

def Reverse_of_number(number):
    #return int(str(number)[::-1])
    rev = 0
    num = number
    while num!=0:
        rem = num%10
        rev = rev*10 + rem
        num = num//10
    return rev

def Reverse_of_string(string):
    #return string[::-1].lower()
    rev = ''
    for i in range(len(string)-1,-1,-1):
        rev = rev + string[i]
    return rev

def Reverse_of_list(List):
    #return List[::-1]
    rev = []
    for i in range(len(List)-1,-1,-1):
        rev.append(List[i])
    return rev

def Reverse_of_tuple(Tuple):
    #return Tuple[::-1]
    rev = []
    for i in range(len(Tuple)-1,-1,-1):
        rev.append(Tuple[i])
    return tuple(rev)


        
