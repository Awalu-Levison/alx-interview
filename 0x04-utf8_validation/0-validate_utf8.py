#!/usr/bin/python3
"""UTF-8 Validation"""


def bit_len(num):
    """Find the bit length"""
    my_bits = 0
    bit_len = 1 << 7
    while bit_len & num:
        my_bits += 1
        bit_len = bit_len >> 1
    return my_bits


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    my_count = 0
    for i in range(len(data)):
        if my_count == 0:
            my_count = get_leading_set_bits(data[i])
            if my_count == 0:
                continue
            if my_count == 1 or my_count > 4:
                return False
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        my_count -= 1
    return my_count == 0
