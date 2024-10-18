#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # Maximum of two numbers: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:

        # check evenneness of a number
        if n % root == 0:
            ops += root
            # set n to the remainder
            n = n / root
            # find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root  until  become evenness
        root += 1
    return ops
