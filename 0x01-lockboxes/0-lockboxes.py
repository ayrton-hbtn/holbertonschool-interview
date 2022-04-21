#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    Iterate over a list of boxes with keys inside.
    Each box may contain keys to other boxes, a key
    with the same number as the index of a box can
    open that box. Determine if all boxes can be opened.
    """
    n = len(boxes)
    if n <= 1:
        return True
    keys = [1]
    for i in range(n - 1):
        keys.append(0)

    for i in range(n):
        if keys[i] == 1:
            for key in boxes[i]:
                try:
                    keys[key] = 1
                except KeyError:
                    pass
        for i in range(n):
            if keys[i] == 1:
                for key in boxes[i]:
                    try:
                        keys[key] = 1
                    except KeyError:
                        pass

    for key in keys:
        if key == 0:
            return False
    return True
