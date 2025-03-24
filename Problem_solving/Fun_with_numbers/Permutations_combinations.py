import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Problem_solving.Fun_with_numbers.Factorial import factorial
def permutation(n, r, rep = False):
    if not rep:
        return factorial(n) // factorial(n - r)
    else:
        return n**r

def combination(n, r):
    return permutation(n, r) // factorial(r)

