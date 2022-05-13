#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Validates a set of characters represented by a list
    of integers.

    Must be UTF-8 Validated.
    Every integer is taken as a byte represented in
    8-bit binary number. The first byte in UTF-8
    is called the significant byte and states the
    number of bytes that the character will have.
    """
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
