#!/usr/bin/python3
"""Solve the task of pascal triangle in python"""


def pascal_triangle(n):
    """Returns the actual tringle"""

    mytriangle = []
    if n > 0:
        mytriangle = [[1]]

        for i in range(1, n):
            """Make rows based on the value of n"""
            row = [1]
            for j in range(1, i):
                row.append(mytriangle[i - 1][j - 1] + mytriangle[i - 1][j])
            row.append(1)
            mytriangle.append(row)
    return mytriangle
