#!/usr/bin/python3
"""this module is responsible to make Determines the winner."""


def isWinner(x, nums):
    """
    Determines the winner after x rounds.
    """
    if x < 1 or not nums:
        return None

    maria_score, ben_score = 0, 0

    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    for n in nums:
        prime_total = sum(primes[0:n + 1])

        if prime_total % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None
