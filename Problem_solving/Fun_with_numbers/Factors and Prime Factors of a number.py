import math

#Time Complexity -- O(n^(1/2))
def factors(number):
    factors = set()
    for i in range(1,int(math.sqrt(number))+1):
        if number % i==0:
            factors = factors.union({i,number//i})
    return factors

#Time Complexity -- O(logn) to O(n)
def Prime_factors(number):
    factors = list()
    if number < 4:
        factors.append(number)
        return factors
    while number>1:
        for i in range(2,number//2+2):
            
            #Check if number is prime
            if i==(1+number // 2):
                factors.append(number)
                number = number // number
                
            #Extract factors and divide number
            if number % i==0:
                factors.append(i)
                number = number // i
                break
    return factors


#Time Complexity -- O(n^(1/2))
def prime_factors_optimized(n):
    factors = []

    # Extract factors of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2  # Reduce n

    # Check odd numbers from 3 to √n
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i  # Reduce n
        i += 2  # Skip even numbers (since even numbers are handled separately)

    # If n is still > 2, it is a prime number
    if n > 2:
        factors.append(n)

    return factors
