#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    Gets fewest number of operations
    """
    # Maximum of two numbers: (min, Copy All => Paste)
    if (n < 2):
        return 0
    sym, root = 0, 2
    while root <= n:

        # check evenneness of a number
        if n % root == 0:
            sym += root
            # set n to the remainder
            n = n / root
            # find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root  until  become evenness
        root += 1
    return sym
