#!/usr/bin/python3
'''This is a module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        previous = triangle[-1]
        current = [1]
        for j in range(1, i):
            current.append(previous[j-1] + previous[j])
        current.append(1)
        triangle.append(current)
    return triangle
