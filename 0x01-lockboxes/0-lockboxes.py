#!/usr/bin/python3

"""
The script determines if all the boxes can be opened
"""

def canUnlockAll(boxes):
    n = len(boxes)

    opened = [False] * n
    opened[0] = True

    queue = [0]
    while queue:
        current = queue.pop(0)
        for keys in boxes[current]:
            if keys < n and not opened[keys]:
                opened[keys] = True
                queue.append(keys)
    return all(opened)
