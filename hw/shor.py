from sympy import isprime # free isprime function
import random



#####################################################
############## Pre-implemented methods ##############
#####################################################

# Dumb period-finding algorithm. Call this for find_factor
# Returns the period of a mod m
def find_period(a,m):
    cur_pow = 1
    # period should be at most m-1
    for r in range(1,m):
        cur_pow = (cur_pow * a) % m
        if cur_pow == 1:
            return r
    # should only be calling find_period on a with gcd(a,m)=1
    assert(False)

print("Testing find_period")
assert(find_period(2,7) == 3)
assert(find_period(2,9) == 6)
assert(find_period(1,100) == 1)
assert(find_period(5,6) == 2)
assert(find_period(2,27) == 18)
assert(find_period(277,3053) == 210)


# Dumb factoring algorithm, used for testing
SMALL = 100
primes = []
for p in range(2,SMALL):
    if isprime(p):
        primes.append(p)

def factor_naive(m):
    if m == 1:
        return []
    if isprime(m):
        return [m]
    ans = []
    for p in primes:
        while (m % p == 0):
            ans = ans + [p]
            m /= p
        if m == 1:
            break

    ans.sort()
    return ans

#####################################################
#####################################################
#####################################################







n = 10000

# Returns gcd of a and b
def gcd(a,b):
    # TODO
    pass

# Test cases
print("Testing gcd")
assert(gcd(24,24) == 24)
assert(gcd(0,3) == 3)
assert(gcd(3,0) == 3)
assert(gcd(5,8) == 1)
assert(gcd(8,5) == 1)
assert(gcd(32,8) == 8)
assert(gcd(20,52) == 4)
assert(gcd(14**100, 6**100) == 2**100)
assert(gcd(14**100, 15**100) == 1)

# if you implement Euclid's algorithm with recursion, this will exceed the recursion
# depth. So try to make your algorithm iterative
assert(gcd(14**1000, 6**1000) == 2**1000)










# Returns t_th root of m, or None if it is not an integer.
def t_th_root(m,t):
    # TODO
    pass 
print("Testing t-th root")
assert(t_th_root(27, 1000) == None)
assert(t_th_root(27,3) == 3)
assert(t_th_root(27,2) == None)
assert(t_th_root(27,1) == 27)
assert(t_th_root(45**1000, 1) == 45**1000)
assert(t_th_root(45**100, 10) == 45**10)
assert(t_th_root(3**10000, 10000) == 3)
assert(t_th_root(3**10000, 100) == 3**100)

# Returns a^b mod m
def pow_mod (a,b,m):
    # TODO
    pass

print("Testing pow_mod")
assert(pow_mod(2,3,5) == 3)
assert(pow_mod(1,3,5) == 1)
assert(pow_mod(2,1000,5) == 1)
assert(pow_mod(2,1000000000000000000000,5) == 1)
assert(pow_mod(2,9000000000000000000000,27) == 1)
assert(pow_mod(2,9000000000000000000001,27) == 2)
assert(pow_mod(2,9000000000000000000004,27) == 16)


# Returns any nontrivial factor of m, or None if m is prime
def find_factor(m):
    # TODO: Implement
    pass 

# Returns a _sorted_ list of the prime factors of m, with multiplicity (see test cases)
def factor(m):
    # TODO: Implement
    pass

# small cases
print("Testing factor on numbers <= 100")
assert(factor(11) == [11])
assert(factor(24) == [2,2,2,3])
assert(factor(27) == [3,3,3])
for m in range(1,SMALL):
    assert(factor(m) == factor_naive(m))

# slightly larger factoring
print("Testing factor on larger numbers")
assert(factor(2**1000) == [2]*1000) 
assert(factor(5**1000) == [5]*1000)
assert(factor(7**5 * 11**3) == [7]*5 + [11]*3)
assert(factor(41*53*61*71) == [41,53,61,71])
