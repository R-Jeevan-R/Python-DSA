def Decimal_to_BaseX(number,base):
    def helper(num):
        if num == 0 or num == 1:
            binary.append(num)
            return binary
        digit = num%base
        binary.append(digit)
        return helper(num//base)
    binary = []
    helper(number)
    return ''.join([str(d) for d in binary[::-1]])
    
