
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import numbers
import math


def is_prime(num):
    '''
    Is the number prime?
    '''
    # print("Is prime? {}".format(num))

    if not isinstance(num, numbers.Number):
        raise "{} is not a number".format(num)

    # Let's do some special cases first
    num = int(num)

    if num < 0:
        raise "{} was negative".format(num)

    if num == 0 or num == 1:
        return False

    if num == 2 or num == 3:
        return True

    factors = get_prime_factors(num)
    # print("Is prime? Factors of {} : {} -> {}".format(num, factors, (len(factors) == 0)))
    return len(factors) == 0


def get_prime_factors(num):
    "Return a list of all prime factors of the number. Will not include the number itself."
    num = int(num)
    # print("Getting factors of {}".format(num))

    if not isinstance(num, numbers.Number):
        raise "{} is not a number".format(num)

    num = int(num)

    if num < 0:
        raise "{} was negative".format(num)

    factors = []
    if num < 4:
        return factors

    # upper_limit = num
    upper_limit = int(math.sqrt(num)) + 1

    # 2 is a special case
    if num % 2 == 0:
        factors.append(2)
        factors.extend(get_prime_factors(num/2))

    # Check all odd numbers between 3 and the upper limit
    for i in range(3, upper_limit + 1, 2):
        # print("Checking {}; num : {}; upper_limit : {}".format(i, num, upper_limit))

        if num % i == 0:
            # print("{} % {} is zero".format(num, i))
            if is_prime(i):
                factors.append(i)
                factors.extend(get_prime_factors(num/i))

    factors = list(set(factors)) # make contents unique

    # Now check all known factors greater than the upper limit
    for i in factors:
        # print("Now checking big factors; factors : {}".format(factors))
        big_factor = int(num/i)
        if i >= big_factor:
            continue
        # print("Num : {}; i : {}; big_factor : {}".format(num, i, big_factor))
        if is_prime(big_factor):
            factors.append(big_factor)

    factors.sort()
    # print("End : factors of {} : {}".format(num, factors))
    return factors


##########################################################################################

# n = 13195
n = 600851475143
factors = list(set(get_prime_factors(n))) # convert via Set to make the list's values unique
factors.sort()
print("Factors of {} : {}".format(n, factors))

print("Euler 3 solution : {}".format(max(factors)))

