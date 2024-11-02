#!/usr/bin/python3
"""Interpreter directive"""


def validUTF8(data):
    """
    Extract list significant bits
    in utf-8 data encoding
    """
    lsb = data & 0xFF

    try:
        data.decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False

    with open('my_file.txt', 'rb') as file:
        content = file.read()
        if validUTF8(content):
            return True
        else:
            return False
