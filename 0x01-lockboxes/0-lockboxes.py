#!/usr/bin/python3
"""Checks if all boxes can be opened given a list of key lists."""


def canUnlockAll(boxes):
    """Checks if all boxes can be opened given a list of key lists.
    Args:
        boxes: A list of lists, where each sublist represents
        the keys a box contains.
    Returns:
      True if all boxes can be opened, False otherwise.
    """
    keys_to_open_boxes = {0}
    checked_boxes = set()
    while keys_to_open_boxes:
        box_to_open = keys_to_open_boxes.pop()
        # print(box_to_open)
        checked_boxes.add(box_to_open)
        # print(checked_boxes)
        keys_to_open_boxes.update(set(boxes[box_to_open]) - checked_boxes)
        print(keys_to_open_boxes)
    return len(checked_boxes) == len(boxes)