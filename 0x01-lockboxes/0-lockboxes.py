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
    if not n:
        return False
    keys = []  # create list of index keys
    for i in range(n):
        keys.append(0)  # default value 0 (no key)
    keys[0] = 1  # first box is opened

    for i in range(n):  # iterate over boxes
        if keys[i] == 1:  # open box if we have the key
            for key in boxes[i]:  # for each key inside that box
                try:
                    keys[key] = 1  # get the key
                except KeyError:
                    pass
        for i in range(n):  # iterate once more to open previous boxes
            if keys[i] == 1:
                for key in boxes[i]:
                    try:
                        keys[key] = 1
                    except KeyError:
                        pass

    for key in keys:  # check if we found all keys
        if key == 0:
            return False  # return false if one key is missing
    return True  # else return true
