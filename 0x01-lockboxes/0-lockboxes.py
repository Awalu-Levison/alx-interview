#!/usr/bin/python3
"""Unlocking the list of lists"""


def canUnlockAll(boxes):
    """This function defines the list of lists
    the list contains key based on particular box
    """

    keys = [0]
    """Denotes the first box in the list"""

    for mykey in keys:
        """iterate through the list"""
        for myboxkey in boxes[mykey]:
            """check if the particular key matches
            with the particular box
            """
            if myboxkey not in keys and myboxkey < len(boxes):
                keys.append(boxes)
    if len(mykey) == len(boxes):
        return True
    return False
