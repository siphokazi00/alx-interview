#!/usr/bin/python3
"""
Determines whether all locked boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened given a list of boxes and their keys.

    Args:
    boxes: A list of lists, where each inner list contains keys to other boxes.

    Returns:
    True if all boxes can be opened, False otherwise.
    """

    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # First box is unlocked
    queue = [0]

    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
