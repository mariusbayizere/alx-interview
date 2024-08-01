#!/usr/bin/python3
"""
Module will be checking on  lockboxes
"""
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened
    """
    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    return len(keys) == len(boxes)
