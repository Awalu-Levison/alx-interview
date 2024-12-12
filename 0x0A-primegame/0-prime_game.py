#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """
    Identify the winner of a prime game
    session with `x`number of rounds.
    """
    if x < 1 or not nums:
        return None
    win1, win2 = 0, 0
    """
    win1: Maria won games
    win2: Ben won games
    """
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        win2 += primes_count % 2 == 0
        win1 += primes_count % 2 == 1
    if win1 == win2:
        return None
    return 'Maria' if win1 > win2 else 'Ben'
