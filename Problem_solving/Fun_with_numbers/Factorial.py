def factorial_recur(number):
    if number in (0,1):
        return number
    return number * factorial_recur(number - 1)

def factorial(number):
    if number in (0,1):
        return 1
    fact = 1
    while number > 0:
        fact *= number
        number -= 1
    return fact