#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened.

    Args:
        boxes (list of lists): List where each index represents a box
        and contains keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if len(boxes) == 0:
        return False

    unlocked_boxes = {0}
    keys = boxes[0]

    while keys:
        new_key = keys.pop()
        if new_key not in unlocked_boxes:
            unlocked_boxes.add(new_key)
            keys.extend(boxes[new_key])

    return len(unlocked_boxes) == len(boxes)
