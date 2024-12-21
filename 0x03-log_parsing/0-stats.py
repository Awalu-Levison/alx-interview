#!/usr/bin/python3
"""This function parses a log from stdin
and displays its metrics based on the
given format
"""

import sys
import re


def print_mydict(total size, mydict):
    """Prints the dictionary of status codes
    parsed from the stdin in assorting order
    Args:
        total_size: the size of the parsed logn from the stdin
        mydict: given status codes
    """
    print("File size: {}".format(total_size))
    for key in sorted(mydict.keys()):
        if mydict[key] != 0:
            print("{}: {}".format(key, mydict[key]))


my_count = 0
total_size = 0
mydict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

try:
    for line in sys.stdin:
        my_log = line.split()
        if len(my_log) > 2:
            my_count += 1
            try:
                my_code = my_log[-2]
                file_size = int(my_log[-1])
                if my_code in mydict.keys():
                    mydict[my_code] += 1
                    total_size += file_size
                    if my_count % 10 == 0:
                        print_mydict(total_size, mydict)
            except Exception:
                continue
finally:
    print_mydict(total_size, mydict)
