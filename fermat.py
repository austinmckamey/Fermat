import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    # This function conducts modular exponentiation, and returns x^y mod N
    # Space complexity - O(nlog(n))
    # Time complexity - O(n^3)
    if y == 0:
        return 1
    z = mod_exp(x, y//2, N)
    if y % 2 == 0:
        return (z ** 2) % N
    else:
        return (x * z ** 2) % N


def fprobability(k):
    # This function determines the probability that N is correctly classified
    # as prime by the Fermat method based off of the iterations k
    # Space complexity - O(1)
    # Time complexity - O(n^2)
    return 1.0 - 1 / (2 ** k)


def mprobability(k):
    # This function determines the probability that N is correctly classified
    # as prime by the Miller-Rabin method based off of the iterations k
    # Space complexity - O(1)
    # Time complexity - O(n^2)
    return 1.0 - 1 / (4 ** k)


def fermat(N, k):
    # This function conducts the Fermat primality test k times, using the mod_exp()
    # method to determine whether N is prime or composite
    # Space complexity - O(1)
    # Time complexity - O(nlog(n))
    for _ in range(k):
        a = random.randint(2, N - 1)
        x = mod_exp(a, N-1, N)
        if x != 1:
            return 'composite'
    return 'prime'


def miller_rabin(N, k):
    # This function conducts the Miller-Rabin primality test k times, using the
    # mod_exp() method to determine whether N is prime or composite
    # Space complexity - O(1)
    # Time complexity - O(nlog^3(n))
    d = N - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        a = random.randint(2, N - 1)
        x = mod_exp(a, d, N)
        if x == 1 or x == N - 1:
            return 'prime'
        while d != N - 1:
            x = (x * x) % N
            d *= 2
            if x == 1:
                return 'composite'
            if x == N - 1:
                return 'prime'
        return 'composite'
