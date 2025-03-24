import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from Problem_solving.Fun_with_numbers.Permutations_combinations import *
def binomial_expansion(a, b, p):
    def handle(a, b, p, r):
        if r == p:
            return 1 * a**0 * b**p
        return combination(p, r) * a**(p - r) * b**r + handle(a, b, p, r + 1)
    if p == 0:
        return 1
    return handle(a, b, p, 0)

